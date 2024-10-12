'''


Challenges assocaited with this here

1) Why is the capacity important? When the hash map exceeds this capacity,

we cannot arbitrarily remove a key - we
need to remove the least recently used one. After we remove it, we need to know what the second least recently used
one was (as it will be the next one to be deleted).


2) How to know which keys have been used?

We need O(1) for both get and put:

So need to use a hashmap here

Use a q for maintaining

Key @ front of q: Least recently used key here
Key @ back of q: Most recently used key

WHen insert a key for first time
    Put it in back of q here




So the most important tasks needed to be done here is basically

1) Insert
When a new key-value pair is added, create a new linked list node and put it at the back.

2) Update
When an existing key is updated or fetched, find its associated linked list node.
Move it to the back, b/c this is the most recently used node here

    - keep a ref to tail, so when we add we can ahcieve O(1) tc

3)
When a new key-value pair is added and the size of the data structure exceeds capacity,
remove the linked list node at the front.
    - keep a ref to head, so can remove from the front, achieve O(1) here



Edge case:

1. Linkedlist is empty here

we call put to create a new key-value pair.
We create a node for this key-value pair, then we need to set it as both the head and tail (since it's the only node).

The cleanest way to handle the empty list case is by using sentinel nodes.

We will have our head and tail attributes both set to dummy nodes. The "real" head will be head.next and the "real"
tail will be tail.prev. These dummy nodes sit just "outside" of our linked list. What is the purpose? We never want
head or tail to be null.



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
    # we will do this line by line here
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
    '''
    We have to move this to the front of the queue here 
    using move_to_head() so that we know it's least recently used 
    '''
    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        node = self.cache[key]
        self.dll.move_to_start(node)

        return node.val
    '''
    1. If key does not exist, create a new key and then add it to map
    or the cache here 
    
    2. If > capacity now, we then goahead and then remove things here 
    using remove_tail here 
    
    3. 
    
    '''
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