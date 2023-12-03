from typing import Self
from aiosqlite import Connection
from ..models import ItemBase, ItemInDB

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class ItemRepository:
    def __init__(self, db):
        self.db: Connection = db
        self.db.row_factory = dict_factory

    async def get_item(self, item_id):
        async with await self.db.execute(
                '''SELECT id, name, category, created, weight, available, expiration FROM item WHERE id = ?''',
                (item_id,)
        ) as cursor:
            async for row in cursor:
                yield ItemInDB(**row)

    async def get_items(self) -> list[ItemInDB]:
        items = []
        async with await self.db.execute(
                '''SELECT id, name, category, created, weight, available, expiration FROM item'''
                ) as cursor:
            async for row in cursor:
                print(row)
                items.append(ItemInDB(**row))

        return items


    async def add_item(self, item: ItemBase) -> None:
        print(item.__dict__)
        await self.db.execute(
                '''INSERT INTO item (name, category, weight, available, expiration) VALUES (:name, :category, :weight, :available, :expiration)''',
                item.__dict__
                )
        await self.db.commit()


    def update_item(self, item):
        pass

    async def delete_item(self, item_id):
        await self.db.execute(
            '''DELETE FROM item WHERE id = ?''',
            item_id
        )
