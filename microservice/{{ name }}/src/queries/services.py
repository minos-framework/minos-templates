from minos.common import (
    AggregateDiff,
)
from minos.cqrs import (
    QueryService,
)
from minos.networks import (
    Request,
    Response,
    ResponseException,
    enroute,
)


class {{ aggregate }}QueryService(QueryService):
    """{{ aggregate }}QueryService class."""

    @enroute.rest.query("/{{ aggregate.lower() }}s", "GET")
    async def get_{{ aggregate.lower() }}(self, request: Request) -> Response:
        """Get a {{ aggregate }} instance.

        :param request: A request instance..
        :return: A response exception.
        """
        raise ResponseException("Not implemented yet!")

    @enroute.broker.event("{{ aggregate }}Created")
    async def {{ aggregate.lower() }}_created(self, request: Request) -> None:
        """Handle the {{ aggregate }} creation events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        diff: AggregateDiff = await request.content()
        print(diff)

    @enroute.broker.event("{{ aggregate }}Updated")
    async def {{ aggregate.lower() }}_updated(self, request: Request) -> None:
        """Handle the {{ aggregate }} update events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        diff: AggregateDiff = await request.content()
        print(diff)

    @enroute.broker.event("{{ aggregate }}Deleted")
    async def {{ aggregate.lower() }}_deleted(self, request: Request) -> None:
        """Handle the {{ aggregate }} deletion events.

        :param request: A request instance containing the aggregate difference.
        :return: This method does not return anything.
        """
        diff: AggregateDiff = await request.content()
        print(diff)