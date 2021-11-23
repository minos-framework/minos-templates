import sys
import unittest

from src import (
    {{ aggregate }},
    {{ aggregate }}CommandService,
)

from minos.networks import (
    Response,
)
from tests.utils import (
    _FakeRequest,
    build_dependency_injector,
)


class Test{{aggregate}}CommandService(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        self.injector = build_dependency_injector()

    async def asyncSetUp(self) -> None:
        await self.injector.wire(modules=[sys.modules[__name__]])

    async def asyncTearDown(self) -> None:
        await self.injector.unwire()

    def test_constructor(self):
        service = {{ aggregate }}CommandService()
        self.assertIsInstance(service, {{aggregate}}CommandService)

    async def test_create_{{ aggregate.lower() }}(self):
        service = {{ aggregate }}CommandService()

        request = _FakeRequest({})
        response = await service.create_{{ aggregate.lower() }}(request)

        self.assertIsInstance(response, Response)

        observed = await response.content()
        expected = {{ aggregate }}(
            created_at=observed.created_at,
            updated_at=observed.updated_at,
            uuid=observed.uuid,
            version=observed.version,
        )

        self.assertEqual(expected, observed)


if __name__ == '__main__':
    unittest.main()
