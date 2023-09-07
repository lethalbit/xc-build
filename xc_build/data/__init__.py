# SPDX-License-Identifier: BSD-3-Clause

import json
from importlib import resources
from pathlib   import Path

from ..config  import (
	SOURCE_DIR, DLD_DIR
)

__all__ = (
	'load_components',
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
