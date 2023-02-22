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
        self.put_order = []

    def put(self, key, item):
        """
            Adds a new item
            to the cache
        """
        if key is not None and item is not None:
            if key not in self.cache_data.keys():
                self.put_order.append(key)

            if len(self.put_order) > FIFOCache.MAX_ITEMS:
                print("DISCARD: {}".format(self.put_order[0]))
                del self.cache_data[self.put_order[0]]
                del self.put_order[0]
            self.cache_data[key] = item

        def get(self, key):
            """
                Gets an item
                stored in the cache
            """
            return self.cache_data.get(key)
