from __future__ import (
    annotations,
)

from pathlib import (
    Path,
)
from uuid import (
    UUID,
)

from minos.aggregate import (
    InMemoryEventRepository,
    InMemorySnapshotRepository,
    InMemoryTransactionRepository,
)
from minos.common import (
    Config,
    DependencyInjector,
    Injectable,
    Lock,
    LockPool,
    SetupMixin,
)
from minos.networks import (
    InMemoryBrokerPublisher,
)
from minos.saga import (
    SagaContext,
    SagaStatus,
)

from src import (
    FooQueryServiceRepository,
)


@Injectable("saga_manager")
class _FakeSagaManager(SetupMixin):
    """For testing purposes."""

    async def run(self, *args, **kwargs) -> UUID:
        """For testing purposes."""


class _FakeSagaExecution:
    def __init__(self, context: SagaContext, status: SagaStatus = SagaStatus.Finished):
        self.context = context
        self.status = status


class FakeLock(Lock):
    """For testing purposes."""

    def __init__(self, key=None, *args, **kwargs):
        if key is None:
            key = "fake"
        super().__init__(key, *args, **kwargs)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return


class FakeLockPool(LockPool):
    """For testing purposes."""

    async def _create_instance(self):
        return FakeLock()

    async def _destroy_instance(self, instance) -> None:
        """For testing purposes."""


def build_dependency_injector() -> DependencyInjector:
    """For testing purposes"""

    return DependencyInjector(
        build_config(),
        [
            _FakeSagaManager,
            InMemoryBrokerPublisher,
            FakeLockPool,
            InMemoryTransactionRepository,
            InMemoryEventRepository,
            InMemorySnapshotRepository,
            FooQueryServiceRepository,
        ],
    )


def build_config() -> Config:
    """For testing purposes"""

    return Config(DEFAULT_CONFIG_FILE_PATH)


DEFAULT_CONFIG_FILE_PATH = Path(__file__).parents[1] / "config.yml"
