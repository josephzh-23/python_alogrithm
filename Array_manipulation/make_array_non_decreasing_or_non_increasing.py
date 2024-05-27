
'''
This is a hard question basically we need to choose here in the code when we see


# choose an index i int he range given above here and then

set the num[i] to nums[i] + 1 or nums[i] -1 here and this is important here

here there we have the code given above

-
'''
from typing import List

from sorting.Heap.max_heap import OwnMaxHeap

''''''
def convertArray( nums: List[int]) -> int:
    def helper(nums):
        # que = []  # stores negative number, to make max heap.


        # and then here we have half of the data here

        # then we have some other data here
        m = OwnMaxHeap()
        res = 0
        for num in nums:
            if m and num < (m.peek()):
                res += abs(num - (m.pop()))


                # heapq.heappush(que, -num)  # reduce max to num, then push back
                m.push(num) # reduce max to num, then push back
            m.push(num)
        return res

    return min(helper(nums), helper(nums[::-1]))

nums = [3, 2, 4, 5, 0]
print(convertArray(nums))


m = OwnMaxHeap()

m.push(3)
m.push(2)
m.push(7)
print(m.pop())