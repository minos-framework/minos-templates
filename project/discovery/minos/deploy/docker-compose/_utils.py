from __future__ import (
    annotations,
)

from pathlib import (
    Path,
)

import yaml


def build_docker_compose(path: Path) -> str:
    """Build Docker Compose file content."""

    if not path.exists():
        raise ValueError("A base Compose file must exist.")

    with path.open() as file:
        data = yaml.safe_load(file)

    container = {
        "restart": "always",
        "build": "external/discovery",
        "ports": ["5567"],
        "depends_on": ["redis"],
        "environment": {"DISCOVERY_SERVICE_DB_HOST": "redis",},
    }

    data["services"]["discovery"] = container

    return yaml.dump(data, sort_keys=False)
