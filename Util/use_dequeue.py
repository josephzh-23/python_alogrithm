import collections

de = collections.deque([1,2,3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

print ("The deque after appending at right is : ")
print (de)
de.popleft()
print(de)