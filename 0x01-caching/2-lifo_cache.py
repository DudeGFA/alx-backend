#!/usr/bin/python3
"""
    Contains class BasicCache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        Caching using LIFO algorithm
    """

    def __init__(self):
        """
            Initialize instance variables
        """
        super().__init__()
        self.last_in = None

    def put(self, key, item):
        """
            Adds a new item
            to the cache
        """
        if key is not None and item is not None:
            if key not in self.cache_data.keys() and len(
                    self.cache_data) >= LIFOCache.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_in))
                del self.cache_data[self.last_in]

            self.cache_data[key] = item
            self.last_in = key

    def get(self, key):
        """
            Gets an item
            stored in the cache
        """
        return self.cache_data.get(key)
