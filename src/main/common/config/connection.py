import os


class ConnectionConfig:
    @classmethod
    def host(cls) -> str:
        return os.getenv("DB_HOST", "127.0.0.1")

    @classmethod
    def port(cls) -> int:
        return os.getenv("DB_PORT", 5432)

    @classmethod
    def db_name(cls) -> str:
        return os.getenv("DB_NAME", "postgres")

    @classmethod
    def user(cls) -> str:
        return os.getenv("DB_USER", "postgres")

    @classmethod
    def password(cls) -> str:
        return os.getenv("DB_PASSWORD", "default")

    @classmethod
    def driver_name(cls) -> str:
        return os.getenv("DB_DRIVER", "postgresql+pg8000")

    @classmethod
    def min_connections(cls) -> int:
        return os.getenv("DB_MIN_CONNECTIONS", 1)

    @classmethod
    def max_connections(cls) -> int:
        return os.getenv("DB_MAX_CONNECTIONS", 2)
