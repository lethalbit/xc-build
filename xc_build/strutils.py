# SPDX-License-Identifier: BSD-3-Clause

import re
import logging as log
from typing    import Union
from io        import StringIO
from os        import SEEK_SET, SEEK_END


__all__ = (
	'expand_variables',
)

def expand_variables(input_text: Union[str, StringIO], variables: dict[str, str]) -> str:
	'''
	This accursed function preforms bash-style variable expansion on the input
	text with the variables in variables

	Parameters
	----------
	input_text : Union[str, StringIO]
		The input text on which to apply variable expansion
	variables : dict[str, str]
		The collection of variables and their values in which to use

	Notes
	-----

	The following expansions are supported:

	* ``${var:-value}``

	   If ``var`` is not defined, expand to ``value``.

	* ``${var:=value}``

	   Much like ``${var:-value}`` but if ``var`` is not defined then it adds it to the known variables.

	* ``${var:+value}``

	   If ``var`` is defined, then expand to ``value``.


	* ``${var:start:len}```

	   Expands to the substring of ``var`` from ``start`` for ``len`` characters.

	* ``${var:start}```

	   Expands to the substring of ``var`` from ``start`` to the end of ``var``.

	* ``${#var}``

	   Expands to the length of ``var``.

	* ``${var/pattern/string}``

	   Replaces the first occurrence of ``pattern`` in ``var`` with ``string``.

	* ``${var//pattern/string}``

	   Replaces all occurrences of ``pattern`` in ``var`` with ``string``.

	* ``${var/#pattern/string}``

	   If ``pattern` is at the start of ``var`` then it is replaced with ``string``.

	* ``${var/#pattern}``

	   If ``pattern` is at the start of ``var`` then it is removed.

	* ``${var/%pattern/string}``

	   If ``pattern`` is at the end of ``var`` then it is replaced with ``string``.

	* ``${var/%pattern}``

	   If ``pattern`` is at the end of ``var`` then it is removed.

	* ``${var#pattern}``

	   Removes the shortest match of ``pattern`` from the start of ``var``.

	* ``${var##pattern}``

	   Removes the longest match of ``pattern`` from the start of ``var``.

	* ``${var%pattern}``

	   Removes the shortest match of ``pattern`` from the end of ``var``.

	* ``${var%%pattern}``

	   Removes the longest match of ``pattern`` from the end of ``var``.

	* ``${var@operator}``

	   Transforms the value of ``var`` according to the ``operator``:

	   * ``U`` - Converts to upper case
	   * ``u`` - Converts first character to upper case if alphabetic
	   * ``L`` - Converts to lower case


	'''

	# This regex is kinda nasty so here is a breakdown
	#  * \$\{ - Matches the start of the variable
	#  * (?P<p0>\w+)? - Optionally matches the variable name
	#  * (?P<op>[\:\#\/\%][\-\=\+\/\#\%]?)? - Optionally matches `:`,`#`,`/`,`%`,`:-`,`:=`,`:+`,`//`,`##`,`%%`
	#  * (?P<p1>\w+)? - Optionally matches either the pattern, value, or start index
	#  * (?P<sep>[\/\:])? - Optionally matches either `:` or `/`
	#  * (?P<p2>\w+)? - Optionally matches either the replacement string, or length
	#  * \} - Matches the end of the variable
	# All in all this lets us match variables matching the examples above in the docs
	VAR_REGEX = re.compile(
		r'(?P<var>'
			r'\$\{'
				r'(?P<p0>\w+)?'
				r'(?P<op>[\:\#\/\%\@][\-\=\+\/\#\%]?)?'
				r'(?P<p1>[\w\s]+)?'
				r'(?P<sep>[\/\:])?'
				r'(?P<p2>[\w\s]+)?'
			r'\}'
		r')'
	)

	obuff = StringIO()
	if isinstance(input_text, StringIO):
		ibuff = input_text
	else:
		ibuff = StringIO(input_text)

	obuff.seek(0, SEEK_SET)

	cur_pos = 0
	for var in VAR_REGEX.finditer(input_text):
		raw, p0, op, p1, sep, p2  = var.groupdict().values()
		start_pos, end_pos = var.span()

		subst = str()

		match (p0, op, p1, sep, p2):
			case (var_name, None, None, None, None):
				subst = variables.get(var_name, '')
			case (var_name, ':-', value, None, None):
				subst = variables.get(var_name, value)
			case (var_name, ':=', value, None, None):
				subst = variables.get(var_name)
				if subst is None:
					subst = variables.setdefault(var_name, default = value)
			case (var_name, ':+', value, None, None):
				subst = value if var_name in variables else ''
			case (var_name, ':', start, ':', length):
				subst = variables.get(var_name, '')[int(start):int(length)]
			case (var_name, ':', start, None, None):
				subst = variables.get(var_name, '')[int(start):]
			case (None, '#', var_name, None, None):
				subst = str(len(variables.get(var_name, '')))
			case (var_name, '/', pattern, '/', string):
				p = re.compile(pattern)
				subst = p.sub(string, variables.get(var_name, ''), count = 1)
			case (var_name, '//', pattern, '/', string):
				p = re.compile(pattern)
				subst = p.sub(string, variables.get(var_name, ''))
			case (var_name, '/#', pattern, None, None):
				val = variables.get(var_name, '')
				res = ''
				if len(val) > len(pattern):
					if val[0:len(pattern)] == pattern:
						res = f'{val[len(pattern):]}'
					else:
						res = val
				subst = res
			case (var_name, '/#', pattern, '/', string):
				val = variables.get(var_name, '')
				res = ''
				if len(val) > len(pattern):
					if val[0:len(pattern)] == pattern:
						res = f'{string}{val[len(pattern):]}'
					else:
						res = val
				subst = res
			case (var_name, '/%', pattern, None, None):
				val = variables.get(var_name, '')
				res = ''
				if len(val) > len(pattern):
					if val[len(val)-len(pattern):] == pattern:
						res = f'{val[:len(val)-len(pattern)]}'
					else:
						res = val
				subst = res
			case (var_name, '/%', pattern, '/', string):
				val = variables.get(var_name, '')
				res = ''
				if len(val) > len(pattern):
					if val[len(val)-len(pattern):] == pattern:
						res = f'{val[:len(val)-len(pattern)]}{string}'
					else:
						res = val
				subst = res
			case (var_name, '@', 'U', None, None):
				subst = variables.get(var_name, '').upper()
			case (var_name, '@', 'u', None, None):
				subst = variables.get(var_name, '')
				subst[0] = subst[0].upper()
			case (var_name, '@', 'L', None, None):
				subst = variables.get(var_name, '').lower()
			case (var_name, '#', pattern, None, None) | (var_name, '##', pattern, None, None):
				val = variables.get(var_name, '')
				res = ''
				if len(val) > len(pattern):
					if val[0:len(pattern)] == pattern:
						res = f'{val[len(pattern):]}'
					else:
						res = val
				subst = res
			case (var_name, '%', pattern, None, None) | (var_name, '%%', pattern, None, None):
				val = variables.get(var_name, '')
				res = ''
				if len(val) > len(pattern):
					if val[len(val)-len(pattern):] == pattern:
						res = f'{val[:len(val)-len(pattern)]}'
					else:
						res = val
				subst = res
			case _:
				subst = raw
				log.warning(f'Bad substitution: `{raw}`')

		ibuff.seek(cur_pos, SEEK_SET)
		obuff.write(ibuff.read(start_pos - cur_pos))
		cur_pos = end_pos

		obuff.write(subst)

	ibuff.seek(cur_pos, SEEK_SET)
	rem = ibuff.seek(0, SEEK_END) - cur_pos
	ibuff.seek(cur_pos, SEEK_SET)
	obuff.write(ibuff.read(rem))
	res = obuff.getvalue()
	obuff.close()
	return res


if __name__ == '__main__':
	txt = 'https://cdn.kernel.org/pub/linux/kernel/v${VERSION:0:1}.x/linux-${VERSION}.tar.xz'
	v = { 'VERSION': '6.4.12' }
	print(expand_variables(txt, v))
