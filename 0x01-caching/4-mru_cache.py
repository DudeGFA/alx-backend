#!/usr/bin/python3
"""
    Contains class BasicCache
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
        Caching using MRU algorithm
    """

    def __init__(self):
        """
            Initialize instance variables
        """
        super().__init__()
        self.MRU = None

    def put(self, key, item):
        """
            Adds a new item
            to the cache
            using MRU algorithm
        """
        if key is not None and item is not None:
            if key not in self.cache_data.keys() and len(
                    self.cache_data) >= MRUCache.MAX_ITEMS:
                print("DISCARD: {}".format(self.MRU))
                del self.cache_data[self.MRU]

            self.cache_data[key] = item
            self.MRU = key

    def get(self, key):
        """
            Gets an item
            stored in the cache
        """
        if key in self.cache_data.keys():
            self.MRU = key
        return self.cache_data.get(key)
