#!/usr/bin/python3
"""
    Contains class BasicCache
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
        Caching using LRU algorithm
    """
    def __init__(self):
        """
            Initialize instance variables
        """
        super().__init__()
        self.use_order = []

    def put(self, key, item):
        """
            Adds a new item
            to the cache
            using LRU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                idx = self.use_order.index(key)
                del self.use_order[idx]
            self.use_order.append(key)

            if len(self.use_order) > LRUCache.MAX_ITEMS:
                print("DISCARD: {}".format(self.use_order[0]))
                del self.cache_data[self.use_order[0]]
                del self.use_order[0]
            self.cache_data[key] = item

    def get(self, key):
        """
            Gets an item
            stored in the cache
        """
        if key in self.cache_data.keys():
            idx = self.use_order.index(key)
            del self.use_order[idx]
            self.use_order.append(key)
        return self.cache_data.get(key)
