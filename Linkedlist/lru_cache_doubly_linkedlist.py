

'''


lru doubly linkedlist

- have pter to both previous and next node here,
- easier than a single linkedlist here

- This is the first one here

- Need O(1) complexity here,

get() :
Intuitively, whenever an item is accessed using get or updated/added using put, it must be moved to the head of the linked list since
it is now the most recently used item.

When the cache exceeds capacity and we need to evict an item, we remove the item from the tail end of the list, as it is the least recently used item.


put():

In the put method, if a key doesn't already exist, we create a new node and add it to the hash map and the linked list. If the size exceeds the capacity,

the tail node is removed both from the linked list and the hash map. If the key does exist, we update the node's value and move the node to the head of the list. The get method checks if the key is in the hash map and, if found, moves the node to the head of the list and returns its value.
'''


class Node:
    def __init__(self, key=0, value=0):
        # initialize a new node with a key, value, and prev/next pointers
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # initialize the LRU cache with a given capacity
        self.cache = {}  # to hold the keys and node addresses
        self.head = Node()  # dummy head node
        self.tail = Node()  # dummy tail node
        self.capacity = capacity  # maximum capacity of the cache
        self.size = 0  # current size of the cache

        # link head and tail dummy nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # retrieves the value of the node with given key if present
        if key not in self.cache:
            return -1  # key not found
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # inserts a new key-value pair or updates the value of an existing key
        if key in self.cache:
            # key exists, update the value
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            # create a new node for the key-value pair
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_head(node)

            self.size += 1
            if self.size > self.capacity:
                # capacity exceeded, remove the least recently used item
                removed_node = self.remove_tail()
                del self.cache[removed_node.key]
                self.size -= 1

    def move_to_head(self, node):
        # moves a node to the front (head) of the cache
        self.remove_node(node)
        self.add_to_head(node)

    def remove_node(self, node):
        # removes a node from the doubly linked list
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_head(self, node):
        # adds a node to the front (head) of the cache right after the dummy head node
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_tail(self):
        # removes the last node of the doubly linked list (before the dummy tail node)
        node = self.tail.prev
        self.remove_node(node)
        return node

# Example of usage:
# cache = LRUCache(capacity=2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))  # returns 1
# cache.put(3, 3)      # evicts key 2
# print(cache.get(2))  # returns -1 (not found)