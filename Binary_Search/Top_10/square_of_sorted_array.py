from typing import List


'''

Dry run of the code here 

- here and then the code is 
- [-4, -1, 0, 3, 10]

4 < 10 

square : 10
result[4] = 100


'''

def sortedSquares( nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
    return result