#!/usr/bin/python3
"""
    Contains class BasicCache
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
        Caching using LFU algorithm
    """

    def __init__(self):
        """
            Initialize instance variables
        """
        super().__init__()
        self.use_order = []
        self.use_freq = {}

    def put(self, key, item):
        """
            Adds a new item to the cache
            using LFU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                idx = self.use_order.index(key)
                del self.use_order[idx]
            self.use_order.append(key)

            if len(self.use_order) > LFUCache.MAX_ITEMS:
                discard_list = [
                    k for k in self.cache_data.keys()
                    if self.use_freq[k] <= min(
                        self.use_freq.values())]
                if len(discard_list) == 1:
                    discard_key = discard_list[0]
                else:
                    for i in range(len(self.use_order)):
                        if self.use_order[i] in discard_list:
                            discard_key = self.use_order[i]
                            break
                print("DISCARD: {}".format(discard_key))
                del self.cache_data[discard_key]
                del self.use_order[self.use_order.index(discard_key)]
                del self.use_freq[discard_key]
            self.cache_data[key] = item
            if key in self.use_freq.keys():
                self.use_freq[key] += 1
            else:
                self.use_freq[key] = 1

    def get(self, key):
        """
            Gets an item stored in the cache
        """
        if key in self.use_freq.keys():
            self.use_freq[key] += 1
        if key in self.cache_data.keys():
            idx = self.use_order.index(key)
            del self.use_order[idx]
            self.use_order.append(key)
        return self.cache_data.get(key)
