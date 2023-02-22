"""
    Contains class BasicCache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """
            Adds a new item
            to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
            Gets an item
            stored in the cache
        """
        return self.cache_data.get(key)
