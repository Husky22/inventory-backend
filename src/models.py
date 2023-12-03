from pydantic import BaseModel
from datetime import datetime, date


class ItemBase(BaseModel):
    name: str
    category: str
    weight: float
    available: float
    expiration: date

class ItemInDB(ItemBase):
    created: datetime
    id: int
