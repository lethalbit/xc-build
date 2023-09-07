# SPDX-License-Identifier: BSD-3-Clause

import argparse
import logging        as log

from rich             import print
from rich.tree        import Tree

from .                import XCBuildAction
from ..core.strutils  import expand_variables
from ..core.netutils  import download_files
from ..core.fileutils import extract_files
from ..data           import (
	load_components,
	component_archive_path, component_source_path
)
from ..config         import (
	DLD_DIR,
)

__all__ = (
	'ComponentsAction',
)

class ComponentsAction(XCBuildAction):
	pretty_name = 'components'
	short_help  = 'Download/Verify components'
	help        = ''
	description = ''

	def _download(self, args: argparse.Namespace) -> int:
		do_dryrun: bool  = args.dryrun
		dl_all: bool     = args.all
		dl_skip: bool    = args.skip_checksum
		dl_clobber: bool = args.clobber
		dl_jobs: int     = args.concurrent_jobs
		dl_targets = list()

		log.info('Downloading components...')
		for name, details in self.components.items():
			dl_url = f'{details["url"]}/{details["filename"]}'

			if not (DLD_DIR / name).exists():
				(DLD_DIR / name).mkdir(parents = True, exist_ok = True)

			if dl_all:
				for v in details['versions']:
					dl_targets.append(
						(
							expand_variables(dl_url, { 'VERSION': v['version'] }),
							component_archive_path(name, v['version'], details['filename']),
							v['sha512sum']
						)
					)
			else:
				dl_targets.append(
					(
						expand_variables(dl_url, { 'VERSION': details['latest'] }),
						component_archive_path(name, details['latest'], details['filename']),
						list(filter(
							lambda v: v['version'] == details['latest'],
							details['versions']
						))[0]['sha512sum']
					)
				)

		log.info(f'{len(dl_targets)} components selected for download...')

		if do_dryrun:
			log.info('Performing dry run')
			for url, p, chcksm in dl_targets:
				log.info(f'{url} => {p} (sha512sum: {chcksm})')
			return 0
		else:
			if dl_skip:
				dl_targets = list(map(lambda t: (t[0], t[1], None), dl_targets))
			return download_files(dl_targets, dl_clobber, dl_jobs)


	def _extract(self, args: argparse.Namespace) -> int:
		ex_all: bool     = args.all
		ex_clobber: bool = args.clobber
		ex_jobs: int     = args.concurrent_jobs
		archives = list()

		log.info('Extracting components...')
		for name, details in self.components.items():
			if ex_all:
				for v in details['versions']:
					archives.append(
						(
							component_archive_path(name, v['version'], details['filename']),
							component_source_path(name, v['version'])
						)
					)
			else:
				archives.append(
					(
						component_archive_path(name, details['latest'], details['filename']),
						component_source_path(name, details['latest'])
					)
				)

		return extract_files(archives, ex_clobber, ex_jobs)

	def _show(self, args: argparse.Namespace) -> int:
		sh_all: bool = args.all

		tree = Tree(
			'[bold]XC-Build Components[/]',
			guide_style = 'blue'
		)

		for name, details in self.components.items():
			node = tree.add(f'[green]{name}[/] (latest: [cyan]{details["latest"]}[/])')
			node.add(f'URL: {details["url"]}')
			if sh_all:
				versions = node.add('Versions')
				for v in details['versions']:
					have = component_archive_path(name, v['version'], details['filename']).exists()
					versions.add(f'{v["version"]: <8}{" - Downloaded" if have else ""}')
			else:
				have = component_archive_path(name, details['latest'], details['filename']).exists()
				node.add(f'Downloaded: { "✔️" if have else "✖️"}')

		print(tree)

		return 0

	def _rm(self, args: argparse.Namespace) -> int:

		return 0

	def __init__(self):
		super().__init__()

		self.subactions = {
			'download': self._download,
			'extract' : self._extract,
			'show'    : self._show,
			'rm'      : self._rm,
		}
		self.components = load_components()

	def register_args(self, parser: argparse.ArgumentParser) -> None:
		subactions = parser.add_subparsers(
			dest     = 'sub_action',
			required = True
		)

		dl_action = subactions.add_parser(
			'download',
			help = 'Download the component sources'
		)

		dl_action.add_argument(
			'--all', '-a',
			action  = 'store_true',
			default = False,
			help    = 'Download all components, not just the latest one'
		)

		dl_action.add_argument(
			'--skip-checksum', '-S',
			action  = 'store_true',
			default = False,
			help    = 'Skip validating the checksum'
		)

		dl_action.add_argument(
			'--dryrun', '-D',
			action  = 'store_true',
			default = False,
			help    = 'Don\'t actually download the files, just print the URLs.'
		)

		dl_action.add_argument(
			'--clobber', '-c',
			action  = 'store_true',
			default = False,
			help    = 'Clobber already downloaded files'
		)

		dl_action.add_argument(
			'--concurrent-jobs', '-j',
			type    = int,
			default = 4,
			help    = 'Number of concurrent downloads to run (default: 4)'
		)

		ex_action = subactions.add_parser(
			'extract',
			help = 'Unpack the component sources'
		)

		ex_action.add_argument(
			'--clobber', '-c',
			action  = 'store_true',
			default = False,
			help    = 'Clobber already extracted archives'
		)

		ex_action.add_argument(
			'--concurrent-jobs', '-j',
			type    = int,
			default = 4,
			help    = 'Number of concurrent extractions to run (default: 4)'
		)

		ex_action.add_argument(
			'--all', '-a',
			action  = 'store_true',
			default = False,
			help    = 'Extract all archives, not just the latest'
		)

		sh_action = subactions.add_parser(
			'show',
			help = 'List components and versions, and if they are downloaded or not'
		)

		sh_action.add_argument(
			'--all', '-a',
			action  = 'store_true',
			default = False,
			help    = 'Show all versions, not just the latest'
		)

		rm_action = subactions.add_parser(
			'rm',
			help = 'Remove component sources'
		)

	def run(self, args: argparse.Namespace) -> int:
		return self.subactions.get(args.sub_action, lambda s, a: 1)(args)
