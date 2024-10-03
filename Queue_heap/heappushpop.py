
import heapq

li1 = [5, 1, 9, 4, 3]

li2 = [5, 7, 9, 4, 3]

heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and then it will pop the smallest element
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li1, 2))
