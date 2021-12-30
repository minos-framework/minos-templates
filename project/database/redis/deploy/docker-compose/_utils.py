from __future__ import (
    annotations, )

from pathlib import (
    Path, )

import yaml


def build_docker_compose(path: Path) -> str:
    """Build Docker Compose file content."""

    if not path.exists():
        raise ValueError("A base Compose file must exist.")

    with path.open() as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    container = {
        "restart": "always",
        "image": "redis:latest",
    }

    data["services"]["redis"] = container

    return yaml.dump(data, sort_keys=False)
