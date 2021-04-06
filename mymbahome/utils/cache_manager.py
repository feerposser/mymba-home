from django.core.cache import cache


def update_cache(key, value, timeout=None):
    cache.set(key, value, timeout=timeout)

