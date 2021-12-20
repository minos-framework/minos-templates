from __future__ import annotations

from pathlib import Path

import yaml


def build_docker_compose(path: Path) -> str:
    """Build Docker Compose file content."""

    if not path.exists():
        raise ValueError("A base Compose file must exist.")

    with path.open() as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    container = {
        "restart": "always",
        "build": "external/api_gateway",
        "ports": [
            "5566"
        ],
        "depends_on": [
            "discovery"
        ],
        "environment": {
            "PYTHONPATH": "/api_gateway",
            "DISCOVERY_SERVICE_HOST": "discovery",
            "API_GATEWAY_DISCOVERY_HOST": "discovery",
        },
    }

    data["services"]["api-gateway"] = container

    return yaml.dump(data, sort_keys=False)
