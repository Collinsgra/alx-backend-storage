#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""

import requests
import redis
from functools import wraps
from typing import Callable

# Initialize Redis client
redis_client = redis.Redis()

def cache_with_expiration(expiration: int):
    def decorator(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(*args, **kwargs):
            url = args[0]
            cache_key = f"count:{url}"
            content_key = f"content:{url}"

            # Increment the count for this URL
            redis_client.incr(cache_key)

            # Check if the content is already cached
            cached_content = redis_client.get(content_key)
            if cached_content:
                return cached_content.decode('utf-8')

            # Fetch the content if not cached
            content = method(*args, **kwargs)

            # Cache the content with expiration
            redis_client.setex(content_key, expiration, content)

            return content
        return wrapper
    return decorator

@cache_with_expiration(10)
def get_page(url: str) -> str:
    response = requests.get(url)
    return response.text
