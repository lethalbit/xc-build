# SPDX-License-Identifier: BSD-3-Clause

from pathlib import Path
from os      import environ

# XDG directories
XDG_HOME        = Path.home()                 if 'XDG_HOME'        not in environ else Path(environ['XDG_HOME'])
XDG_CACHE_DIR   = (XDG_HOME / '.cache')       if 'XDG_CACHE_HOME'  not in environ else Path(environ['XDG_CACHE_HOME'])
XDG_DATA_HOME   = (XDG_HOME / '.local/share') if 'XDG_DATA_HOME'   not in environ else Path(environ['XDG_DATA_HOME'])
XDG_CONFIG_HOME = (XDG_HOME / '.config')      if 'XDG_CONFIG_HOME' not in environ else Path(environ['XDG_CONFIG_HOME'])

# XC-Build specific sub dirs
XC_BUILD_CACHE   = (XDG_CACHE_DIR   / 'xc-build')
XC_BUILD_DATA    = (XDG_DATA_HOME   / 'xc-build')
XC_BUILD_CONFIG  = (XDG_CONFIG_HOME / 'xc-build')

BUILD_DIR  = (XC_BUILD_CACHE / 'build'     )
SOURCE_DIR = (XC_BUILD_CACHE / 'source'    )
DLD_DIR    = (XC_BUILD_CACHE / 'downloaded')


ALL_XC_DIRS = (
    XC_BUILD_CACHE,
    XC_BUILD_DATA,
    XC_BUILD_CONFIG,

	BUILD_DIR,
    SOURCE_DIR,
    DLD_DIR,
)
