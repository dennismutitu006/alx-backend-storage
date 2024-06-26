#!/usr/bin/env python3
"""
create a cache class. In the init method store an instance of the redis client
as a private var named _redis. and flush the instance using the flushdb.
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the no. of calls to a method in a redis key.

    Parameters:
        method: the method to be decorated.

    Returns:
        wrapped function that incr the call count and reurn the original res.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    our class has an init method to initiliaze and store an instnce of redis.
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            this method takes the data arg generetes a random key
            using uuid and store the input data in Redis using the random
            key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, int, float, bytes]:
        """
        Retrieve data from Redis the key and optionally apply a  conversion fn.

        parameters:
            key: The key str to retrieve the data.
            fn: Optional callable to convert the data to desired format

        Returns:
            The retrieved data ,optionally converted by fn or None if !key
        """
        data = self._redis.get(key)

        if data is None:
            return None

        if fn:
            return fn(data)

        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve data from the Redis as a string.

        Parameters:
            key: the key str to retrieve the data

        Returns:
            The retrieved string or none if does not exists.
        """
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> Optional[int]:
        """Do the same as the above but now in int"""
        return self.get(key, lambda x: int(x))
