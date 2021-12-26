from app.db import tires, database
from app.serializers import TireIn


async def add_tire(data_in: TireIn):
    query = tires.insert().values(**data_in.dict())
    return await database.execute(query=query)


async def get_tires(root):
    query = tires.select()
    return list(await database.fetch_all(query=query))


async def get_tire(manufacturer_id: str):
    query = tires.select(tires.c.manufacturer == manufacturer_id)
    return await database.fetch_one(query=query)
