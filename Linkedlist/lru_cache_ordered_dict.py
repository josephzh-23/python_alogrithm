
'''

PopItem() in orderedDict makes sure the
last in first out order here

O(n) for
'''

from collections import OrderedDict

class LRUCache:
    def __init__(self, max_capacity: int):
        self.cache_map = OrderedDict()  # Initialize the ordered dictionary
        self.max_capacity = max_capacity  # Set the maximum capacity of the cache

    def get(self, key: int) -> int:
        if key in self.cache_map:
            self.cache_map.move_to_end(key)  # Mark key as recently used
            return self.cache_map[key]  # Return the value for the key
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.cache_map.move_to_end(key)  # Mark key as recently used
        self.cache_map[key] = value  # Insert or update the key-value pair
        if len(self.cache_map) > self.max_capacity:
            self.cache_map.popitem(last=False)  # Remove the least recently used ite