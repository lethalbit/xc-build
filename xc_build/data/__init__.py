# SPDX-License-Identifier: BSD-3-Clause

import json
from importlib import resources

__all__ = (
    'load_components',
)

def load_components() -> dict:
    return json.loads(
        resources.read_text(__name__, 'components.json')
    )['components']
