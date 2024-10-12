'''
Init the object with capacity here and then get return the value here

Problem here:
    When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item.
For this problem, when there is a tie (i.e., two or more keys with the same frequency),
the least recently used key would be invalidated.

3) Additionally each will have a user counter which ++ every time key is accessed here.
thru get or put operation here. The get or put will have an O(1) operation.

LFU Cache

1) A map that maps keys to their corresponding node which contains the value and frequency of access.
2) A freq_map that maps frequencies to a doubly linked list
 containing all nodes with that frequency.
3) A variable min_freq to keep track of the minimum frequency
 of all keys in the cache for easy access to the least frequently used item.


To determine the least frequently used key,
a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.



'''

from collections import defaultdict


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node(-1, -1)  # Sentinel head node
        self.tail = Node(-1, -1)  # Sentinel tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_first(self, node: Node) -> None:
        """Add a node right after the head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node: Node) -> Node:
        """Remove an existing node from the list."""
        node.prev.next = node.next
        node.next.prev = node.prev
        # Clear the removed node's pointers
        node.next, node.prev = None, None
        return node

    def remove_last(self) -> Node:
        """Remove the last node and return it."""
        return self.remove(self.tail.prev)

    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.head.next == self.tail


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_node_map = defaultdict(Node)
        self.freq_node_list_map = defaultdict(DoublyLinkedList)

    '''
    Retrieves the node from the map using the given key.
    1) If the key is missing or the capacity is 0, returns -1.
    2) If the node is found, it calls the incr_freq method to 
    update the frequency of the node and returns its value.
    
    3) If node is found then call inc_freq() to update freq of the node and return its value 
    '''
    def get(self, key: int) -> int:
        """Get the value of the key if the key exists in the cache."""
        if self.capacity == 0 or key not in self.key_node_map:
            return -1

        node = self.key_node_map[key]
        self._increase_freq(node)
        return node.value


    '''
    Put method: 
    
    If the capacity is 0, the function ends early as no items can be put into the cache.
    1) If the key is present in the map, it updates the value in the corresponding node 
    and increases the frequency by calling incr_freq.
    2) If the key is not present and the cache is at full capacity,
     it removes the least frequently used item by (1) accessing the linked list for the current minimum frequency, (2) removing the last node from that list, and (3) removing the node's key from the map.
    
    3) A new node is created and added to the map and to the frequency map 
    under frequency 1. The min_freq is set to 1.
    
    '''
    def put(self, key: int, value: int) -> None:
        """Set or insert the value if the key is not already present."""
        if self.capacity == 0:
            return

        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.value = value
            self._increase_freq(node)
            return

        if len(self.key_node_map) == self.capacity:
            least_freq_list = self.freq_node_list_map[self.min_freq]
            node_to_remove = least_freq_list.remove_last()
            del self.key_node_map[node_to_remove.key]

        new_node = Node(key, value)
        self._add_node(new_node)
        self.key_node_map[key] = new_node
        self.min_freq = 1  # Reset min_freq to 1 as a new node is added

    def _increase_freq(self, node: Node) -> None:
        """Increase the frequency count of a node."""
        freq = node.freq
        node_list = self.freq_node_list_map[freq]
        node_list.remove(node)
        if node_list.is_empty():
            del self.freq_node_list_map[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        node.freq += 1
        self._add_node(node)

    def _add_node(self, node: Node) -> None:
        """Add a node to the list that corresponds to its frequency count."""
        freq = node.freq
        node_list = self.freq_node_list_map[freq]
        node_list.add_first(node)

# Example of how to use LFUCache:
# cache = LFUCache(capacity)
# value = cache.get(key)
# cache.put(key, value)
