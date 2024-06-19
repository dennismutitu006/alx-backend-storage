#!/usr/bin/env python3
"""
create a cache class. In the init method store an instance of the redis client
as a private var named _redis. and flush the instance using the flushdb.
"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """
    our class has an init method to initiliaze and store an instnce of redis.
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            this method takes the data arg generetes a random key
            using uuid and store the input data in Redis using the random
            key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->
    Union[str, int, float, bytes, None]:
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
