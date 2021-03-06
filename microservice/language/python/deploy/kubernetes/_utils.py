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

    data.extend(
        [
            {"name": "Deploy Image", "import_playbook": "deploy-image.yaml"},
            {"name": "Deploy Pod", "import_playbook": "deploy-pod.yaml"},
        ]
    )

    return yaml.dump(data, sort_keys=False)
