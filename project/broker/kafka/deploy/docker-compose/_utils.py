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

    data["volumes"]["zookeeper"] = {}
    data["volumes"]["kafka"] = {}

    zookeeper_container = {
        "restart": "always",
        "image": "digitalwonderland/zookeeper:latest",
        "volumes": ["zookeeper:/var/lib/zookeeper"],
    }

    kafka_container = {
        "restart": "always",
        "image": "confluentinc/cp-kafka:latest",
        "ports": ["9092"],
        "depends_on": ["zookeeper"],
        "volumes": ["kafka:/kafka/kafka-logs"],
        "environment": {
            "KAFKA_BROKER_ID": 1,
            "KAFKA_ZOOKEEPER_CONNECT": "zookeeper:2181",
            "KAFKA_ADVERTISED_LISTENERS": "PLAINTEXT://kafka:9092,PLAINTEXT_HOST://localhost:29092",
            "KAFKA_LISTENER_SECURITY_PROTOCOL_MAP": "PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT",
            "KAFKA_INTER_BROKER_LISTENER_NAME": "PLAINTEXT",
            "KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR": 1,
        },
    }

    data["services"]["zookeeper"] = zookeeper_container
    data["services"]["kafka"] = kafka_container

    return yaml.dump(data, sort_keys=False)
