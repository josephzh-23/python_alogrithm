'''
Using hashtable we can search really fast here, fast search, fast insertion,
fast deletion and ordered

Ordered: the data has to be ordered to distinguish recently used and longest unused;
Fast Search: we need to be able to find if a key exists in the cache;
Fast Deletion: if the cache is full, we need to delete the last element;
Fast Insertion: We need to insert the data to the head upon each visit.

This is the least we can do here

1.

'''


class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.dummy_start = Node()
        self.dummy_end = Node()
        self.dummy_start.next = self.dummy_end
        self.dummy_end.prev = self.dummy_start
    # this appends to the start of the node here
    def appendleft(self, node) -> Node:
        left, right = self.dummy_start, self.dummy_start.next
        node.next = right
        right.prev = node
        left.next = node
        node.prev = left

        return node

    def remove(self, node) -> Node:
        left, right = node.prev, node.next
        left.next = right
        right.prev = left

        return node

    def move_to_start(self, node):
        return self.appendleft(self.remove(node))

    def pop(self):
        return self.remove(self.dummy_end.prev)

    def peek(self):
        return self.dummy_end.prev.val


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.dll = DLL()

    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        node = self.cache[key]
        self.dll.move_to_start(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.dll.remove(self.cache[key])
            node.val = value
        else:
            node = Node(key, value)
            self.cache[key] = node

        self.dll.appendleft(node)

        if len(self.cache) > self.capacity:
            self.cache.pop(self.dll.pop().key)