"""Dynamic version pulled in pyproject.toml from tool.hatch.version.path """

from __future__ import annotations
from datetime import datetime

VERSION = f"v{datetime.now().strftime("%Y.%m.%d")}"
