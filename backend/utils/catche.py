from typing import Any

from django.core.cache import cache


def get_or_create(key: str, value: Any, timeout: int = 60):
    if not cache.get(data := cache.get(key, None)):
        if callable(value):
            value = value()
        cache.set(key, value, timeout)

    return data
