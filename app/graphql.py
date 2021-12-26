import typing

import strawberry
from app.db_manager import get_tires


@strawberry.type
class Tire:
    manufacturer: str
    season: str
    profile: str


@strawberry.type
class Query:
    tires: typing.List[Tire] = strawberry.field(resolver=get_tires)


schema = strawberry.Schema(query=Query)