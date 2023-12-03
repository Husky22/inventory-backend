from typing import Annotated
from fastapi import Body
from fastapi.routing import APIRouter
from ..models import ItemBase, ItemInDB
from ..repository.item import ItemRepository
from ..uow import UnitOfWork

item_router = APIRouter()


@item_router.get("/items", response_model=list[ItemInDB])
async def read_items():
    async with UnitOfWork() as uow:
        repo = ItemRepository(uow)
        return await repo.get_items()


@item_router.post("/item")
async def add_items(item: ItemBase):
    async with UnitOfWork() as uow:
        repo = ItemRepository(uow)
        return await repo.add_item(item)
