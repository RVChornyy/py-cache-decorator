from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args) -> Any:
        nonlocal cache_storage
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        else:
            print("Calculating new result")
            cache_storage[args] = func(*args)
            return cache_storage[args]
    return wrapper
