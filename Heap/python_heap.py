
'''

Heapq is a min heap, the minimum at the top
'''
import heapq

# this is the min heap here
# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)


print("The created heap is : ", end="")
print(list(li))

heapq.heappush(li, 4)

print("The modified heap after push is : ", end="")
print(list(li))

'''
 removes and returns the smallest element (i.e., the root node) 
 from a min heap after an item is pushed into the heap.
'''
heapq.heappushpop(li, 4)