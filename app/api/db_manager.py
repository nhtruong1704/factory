from app.api.models import FactoryIn
from app.api.db import factories, database


async def add_factory(payload: FactoryIn):
    query = factories.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_factories():
    query = factories.select()
    return await database.fetch_all(query=query)


async def get_factory(id):
    query = factories.select(factories.c.id == id)
    return await database.fetch_one(query=query)


async def delete_factory(id: int):
    query = factories.delete().where(factories.c.id == id)
    return await database.execute(query=query)


async def update_factory(id: int, payload: FactoryIn):
    query = (
        factories
        .update()
        .where(factories.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
