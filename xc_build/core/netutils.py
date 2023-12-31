# SPDX-License-Identifier: BSD-3-Clause
import logging          as log
from pathlib            import Path
from typing             import Optional, Iterable
from hashlib            import sha512
from concurrent.futures import ThreadPoolExecutor
from itertools          import islice


import requests
import rich.progress    as pb


__all__ = (
	'download_files',
)

def download_files(
		files: Iterable[tuple[str, Path, Optional[str]]], clobber: bool = False, concurrent: int = 4,
		skip_checksums: bool = False, mkdir: bool = True, progress: Optional[pb.Progress] = None
) -> bool:
	if progress is None:
		progress = pb.Progress(
			pb.TextColumn('Downloading [bold blue]{task.fields[filename]: <23}', justify = 'left'),
			pb.BarColumn(),
			'[progress.percentage]{task.percentage:>3.1f}%',
			pb.DownloadColumn(),
			pb.TransferSpeedColumn(),
			pb.TimeRemainingColumn()
		)

	def _download(
		task: pb.TaskID, url: str, dest: Path, clobber: bool = False, mkdir: bool = True,
		checksum: Optional[str] = None
	) -> tuple[pb.TaskID, bool]:
		digest = ''

		if mkdir and not dest.parent.exists():
			dest.parent.mkdir(exist_ok = True, parents = True)

		if dest.exists() and not clobber:
			log.info(f'Already have {dest}, skipping')
			progress.remove_task(task)
			return (task, True)

		with requests.get(url, allow_redirects = True) as r:
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
				progress.remove_task(task)
				return (task, False)
		else:
			log.debug(f'sha512sum: {digest}')
		progress.remove_task(task)
		return (task, True)

	futures = list()
	with progress:
		with ThreadPoolExecutor(max_workers = concurrent) as pool:
			for url, dest, checksum in files:
				task = progress.add_task(
					'Downloading', filename = f'{dest.parent.name}/{dest.name}', start = False
				)
				futures.append(pool.submit(
					_download, task, url, dest, clobber, mkdir, None if skip_checksums else checksum
				))

	return all(map(lambda f: f.result()[0], futures))
