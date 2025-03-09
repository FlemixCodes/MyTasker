from motor.motor_asyncio import AsyncIOMotorClient

from my_tasker.config import bot_config


class MongoDB:
    def __init__(
        self,
        database: str,
        host: str = None,
        username: str = None,
        password: str = None,
        my_url: str = None,
        is_local: bool = False,
    ) -> None:
        self._my_url = my_url

        self._host = host
        self._username = username
        self._password = password
        self._database = database

        self.client = None
        self.db = None
        self._connect(is_local)

    def _connect(self, is_local: bool):
        if not is_local and not self._my_url:
            connect_url_auto = (
                "mongodb://{username}:{password}@{host}/?authSource={database}".format(
                    username=self._username,
                    password=self._password,
                    host=self._host,
                    database=self._database,
                )
            )
        elif is_local and not self._my_url:
            connect_url_auto = "mongodb://{host}/?authSource={database}".format(
                host=self._host, database=self._database
            )
        elif self._my_url:
            connect_url_auto = self._my_url

        self.client = AsyncIOMotorClient(connect_url_auto)
        self.db = self.client[self._database]

    async def ping(self):
        return await self.client.admin.command("ping")

    async def insert_one(self, collection: str, document: dict):
        try:
            collection_ = self.db[collection]
            result = await collection_.insert_one(document)
            return result
        except Exception as e:
            return e

    async def insert_many(self, collection: str, document: dict):
        try:
            collection_ = self.db[collection]
            result = await collection_.insert_many(document)
            return result
        except Exception as e:
            return e

    async def find(self, collection: str, document: dict):
        try:
            collection_ = self.db[collection]
            result = await collection_.find(document)
            return result
        except Exception as e:
            return e

    async def find_one(self, collection: str, document: dict):
        try:
            collection_ = self.db[collection]
            result = await collection_.find_one(document)
            return result
        except Exception as e:
            return e

    async def delete_one(self, collection: str, document: dict):
        try:
            collection_ = self.db[collection]
            result = await collection_.delete_one(document)
            return result
        except Exception as e:
            return e

    async def delete_many(self, collection: str, document: dict):
        try:
            collection_ = self.db[collection]
            result = await collection_.delete_many(document)
            return result
        except Exception as e:
            return e


database = MongoDB(
    my_url=bot_config.db_url.get_secret_value(),
    database=bot_config.db_database.get_secret_value(),
)
