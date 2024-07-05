
'''


Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1]
 holds for every i (0-based) such that (0 <= i <= n - 2).

 Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
'''
def howToApproachThis():


    '''
    Basically in this example here, we have one element here where

    Edge cases: return false from this part of the code here
    You can have 1 modificaiton that leads to another modificatino consider

    3.
    You look at 2 elements at a time here
    Imagine the 2 scenarios here
    Case #1
    If you have [5, 7, 3] case 1

    in this case want to change to 5, 7 , 7 and then next we have sth else here
    -
    Case # 2
    if you have the code [2, 7, 3]
    The ideal way is basically [2, 3, 3] is the better option here


    '''


def checkPossibility(self, nums: List[int]) -> bool:
    num_violations = 0
    for i in range(1, len(nums)):

        if nums[i - 1] > nums[i]:

            if num_violations == 1:
                return False

            num_violations += 1

            if i < 2 or nums[i - 2] <= nums[i]:
                nums[i - 1] = nums[i]
            else:
                nums[i] = nums[i - 1]

    return True
