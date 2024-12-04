from redis import Redis
from app.core.config import settings
import json

redis = Redis.from_url(settings.REDIS_URL)

def cache_set(key: str, value: any, expiration: int = 3600):
    return redis.set(key, json.dumps(value), ex=expiration)

def cache_get(key: str):
    value = redis.get(key)
    return json.loads(value) if value else None

def cache_delete(key: str):
    return redis.delete(key)

def cache_invalidate_pattern(pattern: str):
    for key in redis.scan_iter(pattern):
        redis.delete(key)

