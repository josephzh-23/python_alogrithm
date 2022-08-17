import heapq

h = heapq


def topKOccuringElem(arr):

    res = []
    dict = {}

    for num in arr:

        if num not in dict:

            # {num, freq}
            dict[num] = 1
        else:
            dict[num] +=1
