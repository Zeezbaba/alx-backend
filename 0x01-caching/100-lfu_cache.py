#!/usr/bin/python3
"""a class LFUCache that inherits from
BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """a LFU caching system that
    inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.frequency = {}
        self.usage_order = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order[key] = self.usage_order[key] + 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_freq = min(self.frequency.values())
                least_used = [
                        k for k, v in
                        self.frequency.items() if v == least_freq]
                if len(least_used) > 1:
                    lru = min(least_used, key=lambda k: self.usage_order[k])
                else:
                    lru = least_used[0]
                print(f"DISCARD: {lru}")
                del self.cache_data[lru]
                del self.frequency[lru]
                del self.usage_order[lru]

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = 1

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order[key] = self.usage_order[key] + 1
        return self.cache_data[key]
