#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause

from setuptools import setup, find_packages
from pathlib    import Path

REPO_ROOT   = Path(__file__).parent
README_FILE = (REPO_ROOT / 'README.md')

def vcs_ver():
	def scheme(version):
		if version.tag and not version.distance:
			return version.format_with('')
		else:
			return version.format_choice('+{node}', '+{node}.dirty')
	return {
		'relative_to': __file__,
		'version_scheme': 'guess-next-dev',
		'local_scheme': scheme
	}


setup(
	name = 'XC-Build',
	use_scm_version  = vcs_ver(),
	author           = 'Aki \'lethalbit\' Van Ness',
	author_email     = 'nya@catgirl.link',
	description      = 'Cross-compiler build and management tool',
	license          = 'BSD-3-Clause',
	python_requires  = '~=3.10',
	zip_safe         = True,
	url              = 'https://github.com/lethalbit/xc-build',

	long_description = README_FILE.read_text(),
	long_description_content_type = 'text/markdown',

	setup_requires   = [
		'wheel',
		'setuptools',
		'setuptools_scm'
	],

	install_requires  = [
		'Jinja2',
		'rich',
		'requests',
	],

	packages          = find_packages(
		where   = '.',
		exclude = (
			'tests', 'tests.*', 'examples', 'examples.*'
		)
	),
	package_data      = {
		'xc_build.data.toolchains.aarch64.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.aarch64.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.aarch64.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.arm.none-eabi': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.arm.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.avr': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.frv.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.frv.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.frv.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.hppa.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.hppa.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.hppa1_1.hp-hpux10': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.hppa1_1.hp-hpux11': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.hppa2_0.hp-hpux10': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.hppa2_0.hp-hpux11': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.hppa64.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.hppa64.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ia64.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ia64.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ia64.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.lm32.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.m86k.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.m86k.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.m86k.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.microblaze.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.microblaze.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.microblaze.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.mips.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.mips.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.mips.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.mips64.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.mips64.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.mips64.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppc.none-eabi': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppc.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppc.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppc.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppc64.none-eabi': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppc64.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppc64.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppc64.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppc64le.none-eabi': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppc64le.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppc64le.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppc64le.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppcle.none-eabi': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppcle.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppcle.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.ppcle.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.rv32.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.rv32.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.rv32.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.rv64.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.rv64.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.rv64.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.rx.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.rx.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.rx.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.s390.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.s390x.ibm-tpf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.s390x.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.sh4.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.sh4.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.sh4.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.sparc.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.sparc.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.sparc.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.sparc64.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.sparc64.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.sparc64.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.vax.linux-gnu': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.x86_64.none-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.x86_64.unknown-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.x86_64.unknown-linux': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.xtensa.esp32-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.xtensa.lx106-elf': [
			'toolchain.json',
		],
		'xc_build.data.toolchains.xtensa.none-elf': [
			'toolchain.json',
		],
		'xc_build.data': [
			'components.json',
		]
	},

	extras_require    = {
		'dev': [
			'nox',
			'setuptools_scm'
		]
	},

	entry_points       = {
		'console_scripts': [
			'xc-build = xc_build.cli:main',
		]
	},

	classifiers       = [
		'Development Status :: 4 - Beta',

		'Environment :: Console',

		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
		'Intended Audience :: System Administrators',

		'License :: OSI Approved :: BSD License',

		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX :: Linux',

		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',

		'Topic :: Software Development',
	],

	project_urls      = {
		'Documentation': 'https://lethalbit.github.io/xc-build',
		'Source Code'  : 'https://github.com/lethalbit/xc-build',
		'Bug Tracker'  : 'https://github.com/lethalbit/xc-build/issues',
	}
)
