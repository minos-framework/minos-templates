from __future__ import annotations

from pathlib import Path

import yaml


def build_docker_compose(path: Path) -> str:
    """Build Docker Compose file content."""

    if not path.exists():
        raise ValueError("A base Compose file must exist.")

    with path.open() as file:
        data = yaml.safe_load(file)

    container = {
        "image": "docker.io/bitnami/redis:6.2",
        "user": "root",
        "restart": "always",
        "environment": {"ALLOW_EMPTY_PASSWORD": "yes", "REDIS_DISABLE_COMMANDS": "FLUSHDB,FLUSHALL"},
        "volumes": ["redis:/bitnami/redis/data",],
    }

    data["services"]["redis"] = container
    data["volumes"]["redis"] = dict()

    return yaml.dump(data, sort_keys=False)
