

'''
And to work on this problem here we have the code
2. And then if

'''
from typing import List


def findMaxOnes(nums: List[int]):

    maxiCount = 0
    count = 0
    for n in nums:
        if n == 1:
            count+=1
        else:
            count = 0
        maxiCount = max(count, maxiCount)
    print(maxiCount)
nums = [1, 1, 0, 1, 1, 1]
findMaxOnes(nums)






