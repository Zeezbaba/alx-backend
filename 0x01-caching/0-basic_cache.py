#!/usr/bin/python3
"""a class BasicCache that inherits from BaseCaching and is
a caching system. This caching system doesnt have limit
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """caching system that inherit from BaseCaching"""
    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Adds item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """gets an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
