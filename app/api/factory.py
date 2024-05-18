from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import FactoryOut, FactoryIn, FactoryUpdate
from app.api import db_manager
from app.api.service import is_label_present

factory = APIRouter()

@factory.post('/', response_model=FactoryIn, status_code=201)
async def create_factory(payload: FactoryIn):
    for label_id in payload.labels_id:
        if not is_label_present(label_id):
            raise HTTPException(status_code=404, detail=f"Label with given id:{label_id} not found")

    factory_id = await db_manager.add_factory(payload)
    response = {
        'id': factory_id,
        **payload.dict()
    }

    return response

@factory.get('/', response_model=List[FactoryOut])
async def get_factories():
    return await db_manager.get_all_factories()

@factory.get('/{id}/', response_model=FactoryOut)
async def get_factory(id: int):
    factory = await db_manager.get_factory(id)
    if not factory:
        raise HTTPException(status_code=404, detail="factory not found")
    return factory

@factory.put('/{id}/', response_model=FactoryOut)
async def update_factory(id: int, payload: FactoryUpdate):
    factory = await db_manager.get_factory(id)
    if not factory:
        raise HTTPException(status_code=404, detail="Label not found")

    update_data = payload.dict(exclude_unset=True)

    if 'labels_id' in update_data:
        for label_id in payload.labels_id:
            if not is_label_present(label_id):
                raise HTTPException(status_code=404, detail=f"Label with given id:{label_id} not found")

    factory_in_db = FactoryIn(**factory)

    updated_factory = factory_in_db.copy(update=update_data)

    return await db_manager.update_factory(id, updated_factory)

@factory.delete('/{id}/', response_model=None)
async def delete_factory(id: int):
    factory = await db_manager.get_factory(id)
    if not factory:
        raise HTTPException(status_code=404, detail="factory not found")
    return await db_manager.delete_factory(id)