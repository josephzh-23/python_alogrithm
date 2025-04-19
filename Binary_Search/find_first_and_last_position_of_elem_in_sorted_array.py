'''

Let's illustrate the solution approach using a small example:

Suppose we have the sorted array nums as follows and we're trying to find the starting and ending positions of the target value which is 4.

nums = [1, 2, 4, 4, 4, 5, 6]
target = 4
Step 1: Finding the Left Boundary

We use bisect_left(nums, 4) to find the insertion point for the target value 4.

 This function returns the index at which the integer 4 could be inserted to maintain the sorted order of the array. In this example, bisect_left would return 2.

Indeed,
the first occurrence of 4 in nums is at index 2.

Position: 0  1  2  3  4  5  6
nums:     [1, 2, 4, 4, 4, 5, 6]
             ^     ^
Index:       2 (left boundary)
Step 2: Finding the Right Boundary

Next, we find where the integer 5 (target + 1)
would fit into nums by using bisect_left(nums, 4 + 1). This returns the index 5, signifying where we would insert 5, had it not already been in the array.

The index right before 5 is the last occurrence of 4 in nums, which occurs at index 4.

Position: 0  1  2  3  4  5  6
nums:     [1, 2, 4, 4, 4, 5, 6]
                  ^     ^
Index:                4 (right boundary - 1)
Step 3: Determining if target Was Found

Since the left boundary l is 2 and the right boundary r is 5, and l is not equal to r, we conclude that the target was found.

Step 4: Returning the Result

Finally, since l is less than r, we return [l, r - 1], which translates to [2, 4 - 1], resulting in [2, 3].

Therefore, our function returns [2, 3] as the starting and ending positions of the target value 4 in the sorted array nums.

'''

def searchRange(nums, target):

    if not nums:
        return [-1, -1]
    res = [0] * 2

    l = 0; r = len(nums) - 1

    while l <= r:
        m = r + l //2

        if nums[m] >= target:
            r = m - 1
        else:
            l = m + 1