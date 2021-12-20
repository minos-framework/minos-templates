from __future__ import annotations

from pathlib import Path

import yaml


def build_docker_compose(path: Path) -> str:
    """Build Docker Compose file content.."""

    if not path.exists():
        raise ValueError("A base Compose file must exist.")

    with path.open() as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    data["volumes"]["postgres_volume"] = {}

    container = {
        "restart": "always",
        "build": "external/postgres",
        "command": "postgres -c 'max_connections=200'",
        "ports": [
            "5432"
        ],
        "volumes": [
            "postgres_volume:/var/lib/postgresql",
        ],
        "environment": {
            "POSTGRES_USER": "minos",
            "POSTGRES_PASSWORD": "min0s",
        },
    }

    data["services"]["postgres"] = container

    return yaml.dump(data, sort_keys=False)
