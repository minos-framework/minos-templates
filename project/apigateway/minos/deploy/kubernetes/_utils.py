from __future__ import annotations

from pathlib import Path

import yaml


def build_deploy_playbook(path: Path) -> str:
    """Build Deploy Playbook file content."""
    data = None
    if path.exists():
        with path.open() as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

    if data is None:
        data = list()

    data.append(
        {
            "name": "Deploy Minos ApiGateway",
            "import_playbook": "../external/apigateway/playbooks/deploy.yaml",
        }
    )

    return yaml.dump(data, sort_keys=False)
