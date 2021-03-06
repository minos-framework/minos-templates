from __future__ import (
    annotations,
)

from pathlib import (
    Path,
)

import yaml


def build_deploy_playbook(path: Path) -> str:
    """Build Deploy Playbook file content."""
    data = None
    if path.exists():
        with path.open() as file:
            data = yaml.safe_load(file)

    if data is None:
        data = list()

    data.append({"name": "Create Database", "import_playbook": "create-database.yaml"})
    data.append({"name": "Create Query Database", "import_playbook": "create-database.yaml"})

    return yaml.dump(data, sort_keys=False)


def build_docker_compose(path: Path, microservice_name: str) -> str:
    """Build Docker Compose file content."""

    db_creation_path = path.parent / "external/postgres/10-create-database.sql"
    if not db_creation_path.exists():
        raise ValueError("external/postgres/10-create-database.sql script must exist")

    with db_creation_path.open("a") as db_creation_file:
        db_creation_file.write(f"\nCREATE DATABASE {microservice_name}_db;")
        db_creation_file.write(f"\nCREATE DATABASE {microservice_name}_query_db;")

    if not path.exists():
        raise ValueError("A base Compose file must exist.")

    with path.open() as file:
        data = yaml.safe_load(file)

    if "x-microservice-environment" not in data:
        data["x-microservice-environment"] = {
            "MINOS_INTERFACES_BROKER_COMMON_HOST": "kafka",
            "MINOS_DATABASES_DEFAULT_HOST": "postgres",
            "MINOS_DATABASES_QUERY_HOST": "postgres",
            "MINOS_SNAPSHOT_HOST": "postgres",
            "MINOS_DISCOVERY_HOST": "discovery",
        }
    if "x-microservice-depends-on" not in data:
        data["x-microservice-depends-on"] = ["postgres", "kafka", "discovery"]

    microservice_container = {
        "restart": "always",
        "build": {"context": f"microservices/{microservice_name}", "target": "production"},
        "environment": data["x-microservice-environment"],
        "depends_on": data["x-microservice-depends-on"],
    }

    data["services"][f"microservice-{microservice_name}"] = microservice_container

    with path.open("w") as file:
        yaml.dump(data, file, sort_keys=False)

    return ""
