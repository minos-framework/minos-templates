from minos.cqrs import (
    CommandService,
)
from minos.networks import (
    Request,
    Response,
    ResponseException,
    enroute,
)

from ..aggregates import (
    {{ aggregate }},
)


class {{ aggregate }}CommandService(CommandService):
    """{{ aggregate }}CommandService class."""

    @enroute.rest.command("/{{ aggregate.lower() }}s", "POST")
    @enroute.broker.command("Create{{ aggregate }}")
    async def create_{{ aggregate.lower() }}(self, request: Request) -> Response:
        """Create a new ``{{ aggregate }}`` instance.

        :param request: The ``Request`` instance.
        :return: A ``Response`` instance.
        """
        try:
            content = await request.content()
            obj = {{ aggregate }}(**content)
            return Response(obj)
        except Exception:
            raise ResponseException("An error occurred during order creation.")
