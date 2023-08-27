# SPDX-License-Identifier: BSD-3-Clause

from abc import ABCMeta, abstractmethod

__all__ = (
	'XCBuildAction',
)

class XCBuildAction(metaclass = ABCMeta):

	@property
	@abstractmethod
	def pretty_name(self) -> str:
		raise NotImplementedError()

	@property
	@abstractmethod
	def short_help(self) -> str:
		raise NotImplementedError()

	help         = '<HELP MISSING>'
	description  = '<DESCRIPTION MISSING>'

	def __init__(self):
		pass

	@abstractmethod
	def register_args(self, parser):
		raise NotImplementedError('Actions must implement this method')

	@abstractmethod
	def run(self, args):
		raise NotImplementedError('Actions must implement this method')
