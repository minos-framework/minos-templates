from __future__ import annotations

from pathlib import Path

import yaml


def build_deploy_playbook(path: Path) -> str:
    """Build Deploy Playbook file content."""
    data = None
    if path.exists():
        with path.open() as file:
            data = yaml.safe_load(file)

    if data is None:
        data = list()

    data.extend([
        {
            "name": "Deploy Zookeeper",
            "import_playbook": "../external/zookeeper/playbooks/deploy.yaml",
        },
        {
            "name": "Deploy Kafka",
            "import_playbook": "../external/kafka/playbooks/deploy.yaml",
        },
    ])

    return yaml.dump(data, sort_keys=False)
