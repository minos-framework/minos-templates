from __future__ import (
    annotations,
)

from pathlib import (
    Path,
)

import yaml


def build_docker_compose(path: Path) -> str:
    """Build Docker Compose file content."""

    data = dict()
    data["version"] = "3.9"
    data["volumes"] = {}
    data["services"] = {}

    if path.exists():
        with path.open() as file:
            data |= yaml.safe_load(file)

    return yaml.dump(data, sort_keys=False)
