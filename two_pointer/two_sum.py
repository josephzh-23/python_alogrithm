
'''
The input array would be sorted here
Input: numbers = [1, 3, 4, 5, 7, 11], target = 9
Output: [4, 5]
Explanation: The sum of 4 and 5 is 9. Therefore, index1 = 3, index2 = 4. We return [1, 2].
    iF target = 9, 
    1 + 11 = 12 > 9     so decrease j (pter at the end)
    1+ 7 = 8< 9         so increase i
    3+ 7 > 10           so decrease j
'''
# May not use the same element twice here

def twoSum(nums, target):

    l, r = 0, len(nums) -1
    while l < r:
        curSum = nums[l] + nums[r]

        if curSum > target:
            r-=1
        elif curSum < target:
            l +=1
        else:
            return [l +1, r+1]
