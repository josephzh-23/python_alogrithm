import sys


def findFirstNonRepeat(str):
    map = {}

    for i in range(len(str)):

        char = str[i]

        # a => 1
        # b => 2
        if char not in map:
            map[char] = i
        else:
            map[char] = -1

        min = sys.maxsize
        for key in map.keys():

            if key != -1 and map[key] < min:
                min = map[key]


        if min == sys.maxsize:
            return -1
        else:
            return min