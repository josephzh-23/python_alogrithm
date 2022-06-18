import sys


def findFirstNonRepeatingChar(arr):

    min = sys.maxsize
    s = {}
    for num in arr:
        if num not in s:
            s[num] = 1

        else:
            s[num] = -1

