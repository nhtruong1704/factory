from fastapi import FastAPI, APIRouter
import httpx
from fastapi import APIRouter, HTTPException

app = FastAPI(openapi_url="/api/v1/factories/openapi.json", docs_url="/api/v1/factories/docs")

factories_router = APIRouter()

factories = [
    {'factories_id': 1,
     'name': 'SpaceX',
     'description': 'Founded by Elon Musk, SpaceX is an American aerospace manufacturer and space transportation company.',
     'country': 'United States',
     'age': 'Space exploration, satellite manufacturing, rocket engineering'},
    {'factories_id': 2,
     'name': 'Boeing',
     'description': 'Boeing is an American multinational corporation that designs, manufactures, and sells airplanes, rotorcraft, rockets, satellites, telecommunications equipment, and missiles worldwide.',
     'country': 'United States',
     'age': 'Aerospace, defense, rotorcraft'},
    {'factories_id': 3,
     'name': 'Lockheed Martin',
     'description': 'Lockheed Martin is an American aerospace, defense, arms, security, and advanced technologies company.',
     'country': 'United States',
     'age': 'Aerospace, defense, security, advanced technologies'},
    {'factories_id': 4,
     'name': 'Airbus',
     'description': 'Airbus SE is a European multinational aerospace corporation that designs, manufactures, and sells civil and military aeronautical products worldwide.',
     'country': 'Europe',
     'age': 'Aerospace, defense, helicopters'},
    {'factories_id': 5,
     'name': 'Northrop Grumman',
     'description': 'Northrop Grumman Corporation is an American multinational aerospace and defense technology company.',
     'country': 'United States',
     'age': 'Aerospace, defense, technology'}
]


@factories_router.get("/")
async def read_factories():
    return factories


@factories_router.get("/{factories_id}")
async def read_factory(factories_id: int):
    for factory in factories:
        if factory['factories_id'] == factories_id:
            return factory
    return None


app.include_router(factories_router, prefix='/api/v1/factories', tags=['factories'])

if __name__ == '__main__':
    import uvicorn
    import os

    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
