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

    data["volumes"]["kafka_volume"] = {}

    zookeeper_container = {
        "restart": "always",
        "image": "wurstmeister/zookeeper:latest",
    }

    kafka_container = {
        "restart": "always",
        "image": "wurstmeister/kafka:latest",
        "ports": ["9092"],
        "depends_on": ["zookeeper"],
        "volumes": ["kafka_volume:/kafka"],
        "environment": {
            "KAFKA_DELETE_TOPIC_ENABLE": "true",
            "KAFKA_ADVERTISED_HOST_NAME": "kafka",
            "KAFKA_ADVERTISED_PORT": 9092,
            "KAFKA_ZOOKEEPER_CONNECT": "zookeeper:2181",
        },
    }

    data["services"]["zookeeper"] = zookeeper_container
    data["services"]["kafka"] = kafka_container

    return yaml.dump(data, sort_keys=False)
