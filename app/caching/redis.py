import redis
import os
from app.settings import appsettings
from app.exceptions import RedisConnectionException

def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host=os.environ.get("REDIS_HOST", appsettings.redis_host),
            port=os.environ.get("REDIS_PORT", appsettings.redis_port),
            db=0,
            socket_timeout=appsettings.redis_socket_timeout,
        )
        ping = client.ping()
        if ping is True:
            return client
    except (redis.AuthenticationError, redis.ConnectionError) as e:
         raise RedisConnectionException('Cannot connect to redis host: {} {}:{}'.format( e, appsettings.redis_host, appsettings.redis_port ))


redis_client = redis_connect()