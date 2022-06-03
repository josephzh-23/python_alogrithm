# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# basically popLeft is the same as pop(0), for a queue
print(de.popleft())