# SPDX-License-Identifier: BSD-3-Clause

import json
from importlib import resources

__all__ = (
    'get_components',
)

def get_components() -> dict:
    return json.loads(resources.read_text(__name__, 'components.json'))
