#!/usr/bin/env python
# SPDX-License-Identifier: BSD-3-Clause
import sys
from pathlib import Path

try:
	from xc_build.cli import main
except ImportError:
	xc_build_path = Path(sys.argv[0]).resolve()

	if (xc_build_path.parent / 'xc_build').is_dir():
		sys.path.insert(0, str(xc_build_path.parent))

	from xc_build.cli import main

sys.exit(main())
