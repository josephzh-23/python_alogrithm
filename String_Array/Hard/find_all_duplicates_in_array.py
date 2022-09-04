

# Note we want to do this without creating additional space
"""
0   1  2  3  4  5  6  7
[4  3  2  7  8  2  3  1]

    we see 4
    iter 1: 4 -1 = 3    go to 3rd idx (7), flip sign -7

0   1  2  3  4  5  6  7
[4  3  2  -7  8  2  3  1]

      we see 3
     iter 2: 3-1 =2    go to 2nd position, flip sign -> becomes -2 as seen below

0   1  2   3   4  5  6   7
[4  3  -2  -7  8  2  3  1]

     This way next time we see 3, go 3-1 =2 and, we can check 2nd position idx
        if we see <0, we know thsi number has already been seen once,
        so we add it to the duplicate array above
"""

# Time complexity: O (n)
# SC: O (1)        res doesn't coutn here as the extra as said and explained
# Construct an index array

def findAllDuplicatesInArray(nums):

    # check arr first create an array
    res = []

    for n in nums:

        # This is the index we were referring to
        n= abs(n)

        # the first time it's seen
        if nums[n-1] > 0:
            nums[n-1] *= -1
        else:
            res.append(n)

    return res

#Testign
arr = [1, 2, 3, 4,5,7, 4, 4, 7]

arr = findAllDuplicatesInArray(arr)
for c in arr:
    print(c)

