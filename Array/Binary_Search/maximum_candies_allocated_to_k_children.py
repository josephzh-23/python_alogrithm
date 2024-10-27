'''
#
# Maximum candies allocated to k children here
#
#
# Given each elem in the array
# 1. Having an integer k, allocate piles of candies to k children
#
# 2. Each child gets the same number of candies
#
# 3. Each child take at most 1 pile of candies, and some piles may go unused
#
#
# Maximum candies allocated to children here
# 
Say you have candies candies = [4, 7, 12, 19],

# of children k = 3

left = 0, right = 19

We perform binary search. Initially, mid = (0 + 19 + 1) >> 1 is 10. We check if we can distribute 10 candies to each child.

To check the feasibility, we sum up how many children can receive 10 candies:

Pile 1 can be divided into 4 // 10 children, which is 0.
Pile 2 can be divided into 7 // 10 children, which is 0.
Pile 3 can be divided into 12 // 10 children, which is 1.
Pile 4 can be divided into 19 // 10 children, which is 1.
The total number of children who can receive candies is 0 + 0 + 1 + 1 = 2.

Since we can only satisfy 2 children, but we need to satisfy 3, 10 candies per child is too high. So, we set right = mid - 1, which is 9.

'''
def binarySearch(arr, low, high, x):
    low = 0
    while low <= high:

        mid = low + (high - low) // 2


        # do some calculation here ths is important
        mid = sum(candy // mid for candy in arr)
        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1

# ans = max([1, 3, 4 ,5])
# print(ans)
