# SPDX-License-Identifier: BSD-3-Clause
import logging     as log
from argparse      import ArgumentParser, ArgumentDefaultsHelpFormatter, Namespace
from pathlib       import Path

from rich          import traceback
from rich.logging  import RichHandler

from .config       import ALL_XC_DIRS


from .actions.components import ComponentsAction


__all__ = (
	'main',
)

def _setup_logging(args: Namespace = None) -> None:
	level = log.INFO
	if args is not None and args.verbose:
		level = log.DEBUG

	log.basicConfig(
		force    = True,
		format   = '%(message)s',
		datefmt  = '[%X]',
		level    = level,
		handlers = [
			RichHandler(rich_tracebacks = True, show_path = False)
		]
	)

def _init_dirs() -> None:
	for d in ALL_XC_DIRS:
		if not d.exists():
			d.mkdir(parents = True, exist_ok = True)

def main() -> int:
	traceback.install()
	_setup_logging()
	_init_dirs()

	ACTIONS = (
		{ 'name': 'components',    'instance': ComponentsAction() },
	)


	try:


		parser = ArgumentParser(
			formatter_class = ArgumentDefaultsHelpFormatter,
			description     = 'XC-Build cross-compiler toolchain manager',
			prog            = 'xc-build'
		)

		core_options = parser.add_argument_group('Core configuration options')

		core_options.add_argument(
			'--verbose', '-v',
			action = 'store_true',
			help   = 'Enable verbose output'
		)

		action_parser = parser.add_subparsers(
			dest = 'action',
			required = True
		)

		for act in ACTIONS:
			action = act['instance']
			p = action_parser.add_parser(
					action.pretty_name,
					help = action.short_help,
				)
			action.register_args(p)

		args = parser.parse_args()

		_setup_logging(args)

		if args.action is not None:
			act = list(filter(lambda act: act['instance'].pretty_name == args.action, ACTIONS))[0]
			return act['instance'].run(args)

	except KeyboardInterrupt:
		log.info('bye!')
