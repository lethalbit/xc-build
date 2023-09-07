# SPDX-License-Identifier: BSD-3-Clause
import tarfile
import logging          as log
from pathlib            import Path
from typing             import Iterable, Optional
from concurrent.futures import ThreadPoolExecutor


import rich.progress    as pb

__all__ = (
	'extract_files',
)


def extract_files(
	files: Iterable[tuple[Path, Path]], clobber: bool = False, concurrent: int = 4,
	progress: Optional[pb.Progress] = None
) -> bool:
	if progress is None:
		progress = pb.Progress(
			pb.TextColumn('Extracting [bold blue]{task.fields[filename]: <23}', justify = 'left'),
			'{task.completed: >6}',
			pb.BarColumn(),
			'[progress.percentage]{task.percentage:>3.1f}%',
			pb.TimeElapsedColumn()
		)

	def _extract(task: pb.TaskID, src: Path, dest: Path, clobber: bool) -> tuple[pb.TaskID, bool]:
		def _strip_path(tar: tarfile.TarFile) -> list[tarfile.TarInfo]:
			files = list()
			for m in tar.getmembers():
				p = Path(m.path)
				m.path = Path(*p.parts[1:])
				files.append(m)
			return files

		if not src.exists():
			log.warning(f'File {src.name} does not exist!')
			progress.remove_task(task)
			return (task, False)

		if dest.exists() and not clobber:
			log.info(f'Already extracted \'{src.name}\', skipping')
			progress.remove_task(task)
			return (task, False)


		with tarfile.open(src, 'r:*') as tar:
			members = _strip_path(tar)
			progress.update(task, total = len(members))
			progress.start_task(task)
			for t in members:
				tar.extract(
					t, dest, set_attrs = (not t.isdir()), numeric_owner = False
				)
				progress.advance(task)

		progress.remove_task(task)
		return (task, True)


	futures = list()
	with progress:
		with ThreadPoolExecutor(max_workers = concurrent) as pool:
			for src, dest in files:
				task = progress.add_task(
					'Extracting', filename = f'{dest.parent.name}/{dest.name}', start = False
				)
				futures.append(pool.submit(
					_extract, task, src, dest, clobber
				))

	return all(map(lambda f: f.result()[0], futures))
