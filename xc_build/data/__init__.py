# SPDX-License-Identifier: BSD-3-Clause

import json
from importlib       import resources
from typing          import Optional
from pathlib         import Path

from ..core.strutils import expand_variables
from ..config        import (
	SOURCE_DIR, DLD_DIR
)

__all__ = (
	'load_components',
	'get_paths',
	'component_archive_path',
	'component_source_path'
)

def component_archive_path(name: str, version: str, filename: str) -> Path:
	return (
		(DLD_DIR / name) / f'{version}{"".join(Path(filename).suffixes)}'
	)

def component_source_path(name: str, version: str) -> Path:
	return (
		(SOURCE_DIR / name) / version
	)

def load_components() -> dict:
	return json.loads(
		resources.read_text(__name__, 'components.json')
	)['components']


def get_paths(components: Optional[dict] = None, for_all: bool = False) -> list[dict]:
	if components is None:
		components = load_components()

	component_paths = list()

	for name, details in components.items():
		if for_all:
			for ver in details['versions']:
				component_paths.append({
					'component': name,
					'url': expand_variables(
						f'{details["url"]}/{details["filename"]}', {'VERSION': ver['version']}
					),
					'version': ver['version'],
					'archive_path': component_archive_path(name, ver['version'], details['filename']),
					'source_path': component_source_path(name, ver['version']),
					'sha512sum': ver['sha512sum']
				})
		else:
			component_paths.append({
				'component': name,
				'url': expand_variables(
					f'{details["url"]}/{details["filename"]}', {'VERSION': details['latest']}
				),
				'version': details['latest'],
				'archive_path': component_archive_path(name, details['latest'], details['filename']),
				'source_path': component_source_path(name, details['latest']),
				'sha512sum': list(filter(
					lambda v: v['version'] == details['latest'],
					details['versions']
				))[0]['sha512sum']
			})

	return component_paths
