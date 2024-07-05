'''

Given an array of n integers,

max sum possible of all length of squares

arr[] = {5, 3, 2, 3, 6, 3, 3}
'''
from collections import Counter

'''
sort the array in reverse order
count the occurrences of each number -> dict
if number is even, keep
if number is odd, e.g., 1,3,5
    
    Check if num -1 exists in the dict, move 1 to num -1 
    repeat the process until we reach the end of the array 
    
get all the keys with even number of occurrences, pair them in the reverse order
'''
    #step3 : Convert the frequencies to single dimensional array in descending order.
c = [2,3,3,4,6,8,8,6]
# findSumLength(c, len(c))


def maximumRectangle(array):
    if len(array) < 4:
        return 0
    array = sorted(array, reverse=True)
    pair1 = -1
    totalSum = 0
    idx = 0

    while idx < len(array):
        if idx + 1 < len(array):
            # this is when they are the same
            if array[idx] - array[idx + 1] <= 1:
                if pair1 == -1:

                    # not set yet? then set it to the minum
                    pair1 = min(array[idx], array[idx + 1])
                else:
                    totalSum += pair1 * min(array[idx], array[idx + 1])
                    pair1 = -1
                idx += 1
        idx += 1
    return totalSum

print(maximumRectangle(c))
