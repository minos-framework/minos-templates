from __future__ import annotations

from pathlib import Path

import yaml


def build_docker_compose(path: Path) -> str:
    """Build Docker Compose file content."""

    if not path.exists():
        raise ValueError("A base Compose file must exist.")

    with path.open() as file:
        data = yaml.safe_load(file)

    data["volumes"]["zookeeper"] = {}
    data["volumes"]["kafka"] = {}

    zookeeper_container = {
        "restart": "always",
        "image": "digitalwonderland/zookeeper:latest",
        "volumes": ["zookeeper:/var/lib/zookeeper"],
    }

    kafka_container = {
        "restart": "always",
        "image": "wurstmeister/kafka:latest",
        "ports": ["9092"],
        "depends_on": ["zookeeper"],
        "volumes": ["kafka:/kafka/kafka-logs"],
        "environment": {
            "KAFKA_LOG_DIRS": "/kafka/kafka-logs",
            "KAFKA_DELETE_TOPIC_ENABLE": "true",
            "KAFKA_ZOOKEEPER_CONNECT": "zookeeper:2181",
            "KAFKA_ADVERTISED_HOST_NAME": "kafka",
        },
    }

    data["services"]["zookeeper"] = zookeeper_container
    data["services"]["kafka"] = kafka_container

    return yaml.dump(data, sort_keys=False)
