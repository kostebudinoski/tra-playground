from app.caching.redis import redis_client
from datetime import timedelta

def get_model_version(source_lang: str, target_lang: str) -> str:
    MODEL_VERSION_NAME = "1.2.3"

    key = f"{source_lang}:{target_lang}"
    model_version = redis_client.get(key)
    if model_version is not None:
        return model_version
    else:
        redis_client.set(key, MODEL_VERSION_NAME, timedelta(minutes=24 * 60))
        return MODEL_VERSION_NAME