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

    data.append({"name": "Deploy Namespace", "import_playbook": "deploy-namespace.yaml"})

    return yaml.dump(data, sort_keys=False)
