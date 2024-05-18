from pydantic import BaseModel
from typing import List, Optional


class FactoryIn(BaseModel):
    name: str
    description: str
    country: str
    age: str
    workers_id: List[int]


class FactoryOut(FactoryIn):
    id: int


class ArtistUpdate(FactoryIn):
    name: Optional[str] = None
    description: Optional[str] = None
    country: Optional[str] = None
    age: Optional[str] = None
    workers_id: Optional[List[int]] = None