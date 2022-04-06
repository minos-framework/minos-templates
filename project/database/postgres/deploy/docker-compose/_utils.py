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

    data["volumes"]["postgres"] = {}

    container = {
        "restart": "always",
        "build": "external/postgres",
        "command": "postgres -c 'max_connections=200'",
        "ports": ["5432:5432"],
        "volumes": ["postgres:/var/lib/postgresql/data",],
        "environment": {"POSTGRES_USER": "minos", "POSTGRES_PASSWORD": "min0s",},
    }

    data["services"]["postgres"] = container

    return yaml.dump(data, sort_keys=False)
