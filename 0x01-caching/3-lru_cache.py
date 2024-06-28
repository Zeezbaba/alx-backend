#!/usr/bin/python3
"""a class LRUCache that inherits from
BaseCaching and is a caching system
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching system that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove the existing key to update its position
            self.cache_data.pop(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the least recently used item
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            self.cache_data.pop(first_key)

        # Insert the item as the most recently used
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end to mark it as recently used
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
