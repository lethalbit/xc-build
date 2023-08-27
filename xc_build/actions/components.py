# SPDX-License-Identifier: BSD-3-Clause

import argparse
import tarfile
import logging   as log

from pathlib     import Path
from typing      import Optional

from rich        import print
from rich.tree   import Tree

from .           import XCBuildAction
from ..strutils  import expand_variables
from ..data      import get_components
from ..config    import (
	XC_BUILD_CONFIG,
	SOURCE_DIR,
	DLD_DIR,
)

__all__ = (
	'ComponentsAction',
)

def _download_file(url: str, dest: Path, checksum: Optional[str] = None) -> bool:
	from hashlib import sha512
	import requests
	import rich.progress as pb

	if dest.exists():
		log.info(f'Already have {dest}, skipping')
		return True

	with pb.Progress(
		pb.TextColumn('Downloading [bold blue]{task.fields[filename]: <23}', justify = 'left'),
		pb.BarColumn(),
		'[progress.percentage]{task.percentage:>3.1f}%',
		' ',
		pb.DownloadColumn(),
		' ',
		pb.TransferSpeedColumn(),
		' ',
		pb.TimeRemainingColumn()
	) as progress:
		with requests.get(url, allow_redirects = True) as r:
			task = progress.add_task('download', filename = f'{dest.parent.name}/{dest.name}', start = True)
			h = sha512()
			progress.update(task, total = int(r.headers['Content-length']))
			with open(dest, 'wb') as f:
				progress.start_task(task)
				for chunk in r.iter_content(chunk_size = 8192):
					f.write(chunk)
					h.update(chunk)
					progress.update(task, advance = len(chunk))

	digest = h.hexdigest()

	log.debug(f'Downloaded \'{dest.name}\'')
	if checksum is not None:
		log.debug('Checking digest...')
		if digest != checksum:
			log.error(f'File checksum failed! got: {digest} wanted: {checksum}')
			return False
	else:
		log.debug(f'sha512sum: {digest}')
	return True


def _cmp_dl_path(comp: str, ver: str, fname: str) -> Path:
	return ((DLD_DIR / comp) / f'{ver}{"".join(Path(fname).suffixes)}')

class ComponentsAction(XCBuildAction):
	pretty_name = 'components'
	short_help  = 'Download/Verify components'
	help        = ''
	description = ''

	def _download(self, args: argparse.Namespace) -> int:
		do_dryrun: bool = args.dryrun
		dl_all: bool    = args.all
		dl_skip: bool   = args.skip_checksum

		dl_targets = list()


		for name, details in self.components.items():
			dl_url = f'{details["url"]}/{details["filename"]}'

			if not (DLD_DIR / name).exists():
				(DLD_DIR / name).mkdir(parents = True, exist_ok = True)

			if dl_all:
				for v in details['versions']:
					dl_targets.append(
						(
							expand_variables(dl_url, { 'VERSION': v['version'] }),
							_cmp_dl_path(name, v['version'], details['filename']),
							v['sha512sum']
						)
					)
			else:
				dl_targets.append(
					(
						expand_variables(dl_url, { 'VERSION': details['latest'] }),
						_cmp_dl_path(name, details['latest'], details['filename']),
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
			if do_dryrun:
				log.info(f'{url} => {p} (sha512sum: {chcksm})')
			else:
				_download_file(url, p, None if dl_skip else chcksm)


		return 0

	def _extract(self, args: argparse.Namespace) -> int:
		def _strip_path(tar: tarfile.TarFile):
			files = list()
			for m in tar.getmembers():
				p = Path(m.path)
				m.path = Path(*p.parts[1:])
				files.append(m)
			return files

		for name, details in self.components.items():
			cmpt_dir: Path = (SOURCE_DIR / name)

			if not cmpt_dir.exists():
				cmpt_dir.mkdir(parents = True, exist_ok = True)

			for v in details['versions']:
				cmpt = _cmp_dl_path(name, v['version'], details['filename'])
				if cmpt.exists():
					log.info(f'Extracting {name}/{cmpt.name} to {cmpt_dir}')
					with tarfile.open(cmpt, 'r:*') as tar:
						tar.extractall(cmpt_dir / v['version'], members = _strip_path(tar))


		return 0

	def _show(self, args: argparse.Namespace) -> int:
		tree = Tree(
			'[bold]XC-Build Components[/]',
			guide_style = 'blue'
		)

		for name, details in self.components.items():
			node = tree.add(f'[green]{name}[/] (latest: [cyan]{details["latest"]}[/])')
			node.add(f'URL: {details["url"]}')
			versions = node.add('Versions')
			for v in details['versions']:
				have = _cmp_dl_path(name, v['version'], details['filename']).exists()
				versions.add(f'{v["version"]: <8}{" - Downloaded" if have else ""}')

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
		self.components = get_components()['components']

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

		ex_action = subactions.add_parser(
			'extract',
			help = 'Unpack the component sources'
		)

		sh_action = subactions.add_parser(
			'show',
			help = 'List components and versions, and if they are downloaded or not'
		)

		rm_action = subactions.add_parser(
			'rm',
			help = 'Remove component sources'
		)

	def run(self, args: argparse.Namespace) -> int:
		return self.subactions.get(args.sub_action, lambda s, a: 1)(args)
