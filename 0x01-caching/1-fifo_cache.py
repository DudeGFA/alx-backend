#!/usr/bin/python3
"""
    Contains class BasicCache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        Caching using FIFO algorithm
    """
    def __init__(self):
        """
            Initialize instance variables
        """
        super().__init__()
        self.put_order = {}

    def put(self, key, item):
        """
            Adds a new item
            to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        else:
            return

        if len(self.cache_data.keys()) > FIFOCache.MAX_ITEMS:
            print("DISCARD: {}".format(self.put_order[0]))
            del self.cache_data[self.put_order[0]]
            self.put_order[0] = self.put_order[1]
            self.put_order[1] = self.put_order[2]
            self.put_order[2] = self.put_order[3]
            del self.put_order[3]
        self.put_order[len(self.put_order)] = key

    def get(self, key):
        """
            Gets an item
            stored in the cache
        """
        return self.cache_data.get(key)
