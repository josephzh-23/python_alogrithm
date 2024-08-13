

#
import sys


'''
    May seem easy but kind of hard
'''
# Why do we need -1? Because there could be a case
# where all characters are unique
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

    min = sys.maxsize

    # for
    for key in map.keys():
        print(key)
        # meaning it's unique (not -1)
        if -1 < map[key] < min:

            # store the index of the value passed
            min = map[key]

    if min == sys.maxsize:
        return -1
    else:
        return min

arr = [1,1, 2, 3, 4, 4, 5]
print(findFirstNonRepeatingChar(arr))