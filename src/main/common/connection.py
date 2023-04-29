import logging
from abc import ABC, abstractmethod
from typing import Optional, Union
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, URL
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker, Session, close_all_sessions

from src.main.common.config.connection import ConnectionConfig

logger = logging.getLogger("slack_app")


class AbstractConnection(ABC):
    def __init__(self, override_url=None):
        self.override_url = override_url
        self._engine: Optional[Union[AsyncEngine, Engine]] = None
        self._session_maker: Optional[sessionmaker] = None
        self._session: Optional[Union[AsyncSession, Session]] = None

    def _connection_str(self) -> URL:
        if self.override_url:
            return self.override_url

        return sqlalchemy.engine.url.URL.create(
            drivername=ConnectionConfig.driver_name(),
            username=ConnectionConfig.user(),
            password=ConnectionConfig.password(),
            host=ConnectionConfig.host(),
            port=ConnectionConfig.port(),
            database=ConnectionConfig.db_name(),
        )

    def get_session(self) -> Union[AsyncSession, Session]:
        self._initialize()
        if self._session is None:
            self._session = self._session_maker()
        return self._session

    def get_engine(self) -> Union[AsyncEngine, Engine]:
        self._initialize()
        return self._engine

    @abstractmethod
    def _teardown(self, close_sessions: bool = False) -> None:
        pass

    @abstractmethod
    def _initialize(self) -> None:
        pass


class Connection(AbstractConnection):
    """
    Object for managing and setting up connections with postgres
    """

    def _initialize(self) -> None:
        if self._engine is None:
            self._engine: Engine = create_engine(
                self._connection_str(),
                pool_size=int(ConnectionConfig.min_connections()),
                max_overflow=int(ConnectionConfig.max_connections()),
                pool_pre_ping=True,
            )
            self._session_maker = sessionmaker(bind=self._engine)

    def _teardown(self, close_sessions: bool = False) -> None:
        if close_sessions:
            close_all_sessions()
        elif self._session is not None:
            self._session.close()

        self._engine = None
        self._session_maker = None
        self._session = None
