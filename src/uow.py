import aiosqlite
from aiosqlite import Connection
from .config import DB_CONNECTION

class UnitOfWork:
    def __init__(self):
        self.db: None | Connection = None


    async def __aenter__(self):
        self.db = await aiosqlite.connect(DB_CONNECTION)
        return self.db

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if isinstance(self.db, Connection):
            await self.db.close()



