"""
Aka: priority queue In a heap, the highest (or lowest) priority element
 is always stored at the root.

minHeap: the root is the min value
maxHeap: the root is the max value


        heap should be used when Use it whenever you need quick access
        to the largest (or smallest)
 item, because that item will always be the first element
  in the array or at the root of the tree

- An elem of highgest priority appear at the front
TC:
1. Insert/Delete    O(logN)     very fast
2.
"""

# Python code to demonstrate working of
# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)


print("The created heap is : ", end="")
print(list(li))

heapq.heappush(li, 4)

print("The modified heap after push is : ", end="")
print(list(li))

# print("The popped and smallest element is : ", end="")
# print(heapq.heappop(li))