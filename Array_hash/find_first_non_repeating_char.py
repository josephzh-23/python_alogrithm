

#
import sys


def findFirstNonRepeatingChar(str):

    map = {}
    for i in range(len(str)):
        char = str[i]

        # a => 1
        # b => 2
        if char not in map:
            map[char] = i
        # duplicate already found
        else:
            map[char] = -1

        # find the
    min = sys.maxsize

    for key in map.keys():
        # meaning it's not a duplicate
        if map[key] > -1 and map[key] < min:

            # store the index of the array that's passed
            min = map[key]

    if min == sys.maxsize:
        return -1
    else:
        return min

arr = [1,1, 2, 3, 4, 4, 5]
print(findFirstNonRepeatingChar(arr))