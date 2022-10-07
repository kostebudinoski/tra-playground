from pydantic import BaseSettings

class AppSettings(BaseSettings):
    db_connection_string: str = "sqlite:///./rating-db.db"
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_socket_timeout: int = 5


appsettings = AppSettings()