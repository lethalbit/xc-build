# SPDX-License-Identifier: BSD-3-Clause

import argparse
import logging        as log

from pathlib          import Path
from shutil           import rmtree

from rich             import print
from rich.prompt      import Confirm
from rich.tree        import Tree
from rich.progress    import track

from .                import XCBuildAction
from ..core.netutils  import download_files
from ..core.fileutils import extract_files
from ..data           import load_components, get_paths, component_archive_path


__all__ = (
	'ComponentsAction',
)

class ComponentsAction(XCBuildAction):
	pretty_name = 'components'
	short_help  = 'Download/Verify components'
	help        = ''
	description = ''

	def _download(self, args: argparse.Namespace) -> int:
		dl_all: bool     = args.all
		dl_skip: bool    = args.skip_checksum
		dl_clobber: bool = args.clobber
		dl_jobs: int     = args.concurrent_jobs

		log.info('Downloading components...')
		dl_targets = get_paths(self.components, dl_all)

		log.info(f'{len(dl_targets)} components selected for download...')

		return download_files(
			map(
				lambda t: (t['url'], t['archive_path'], t['sha512sum']),
				dl_targets,
			), dl_clobber, dl_jobs, dl_skip
		)


	def _extract(self, args: argparse.Namespace) -> int:
		ex_all: bool     = args.all
		ex_clobber: bool = args.clobber
		ex_jobs: int     = args.concurrent_jobs

		log.info('Extracting components...')
		archives = get_paths(self.components, ex_all)

		return extract_files(
			map(
				lambda a: (a['archive_path'], a['source_path']),
				archives,
			), ex_clobber, ex_jobs
		)

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
		rm_all:     bool = args.all
		rm_archive: bool = args.remove_archives

		targets = get_paths(self.components, rm_all)

		if Confirm.ask(f'You are about to remove {len(targets)} components, are you sure?', default = 'n'):
			for t in track(targets, description = 'Deleting components...'):
				archive: Path = t['archive_path']
				sources: Path = t['source_path']

				if archive.exists() and rm_archive:
					log.debug(f'removing {archive}')
					archive.unlink()

				if sources.exists():
					log.debug(f'removing {sources}')
					rmtree(sources)

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

		rm_action.add_argument(
			'--all', '-a',
			action  = 'store_true',
			default = False,
			help    = 'Remove all components, not just the latest'
		)

		rm_action.add_argument(
			'--remove-archives', '-A',
			action  = 'store_true',
			default = False,
			help    = 'Also remove the downloaded component archive, not just the source dir'
		)

	def run(self, args: argparse.Namespace) -> int:
		return self.subactions.get(args.sub_action, lambda s, a: 1)(args)
