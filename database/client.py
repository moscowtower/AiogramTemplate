from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


class Client:
    def __init__(
        self,
        username: str,
        password: str,
        host: str,
        name: str
    ) -> None:
        self.username = username
        self.password = password
        self.host = host
        self.name = name

        self.engine = create_engine(
            self.engine_string(),
            pool_size=50,
            max_overflow=100,
            pool_recycle=3600

        )

        self.async_engine = create_async_engine(
            self.engine_string(async_engine=True),
            pool_size=50,
            max_overflow=100,
            pool_recycle=3600
        )

        self.Session = sessionmaker(bind=self.engine)
        self.AsyncSession = sessionmaker(
            bind=self.async_engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    def engine_string(self, async_engine: bool = False):
        return "mysql+{}://{}:{}@{}/{}".format(
            "aiomysql" if async_engine else "mysqldb",
            self.username,
            self.password,
            self.host,
            self.name
        )
