#!/usr/bin/python3
"""a class FIFOCache that inherits from
BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A caching system that inherits from BaseCaching"""
    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Adds item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.cache_data.keys():
            firstKey = next(iter(self.cache_data.keys()))
            del self.cache_data[firstKey]
            print("DISCARD: {}".format(firstKey))

        self.cache_data[key] = item

    def get(self, key):
        """Gets item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
