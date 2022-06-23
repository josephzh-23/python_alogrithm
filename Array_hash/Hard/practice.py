import heapq
import sys


def findFirstNonRepeatingChar(arr):

    min = sys.maxsize
    s = {}
    for num in arr:
        if num not in s:
            s[num] = 1

        else:
            s[num] = -1

q= heapq
def topKMostFrequentElement(arr):
    # <char, freq>
    map = {}
    minHeap = []
    q.heapify(minHeap)
    for char in arr:
        if char not in map:
            map[char] = 1
        else:
            map[char] +=1


    # loop thru map
    for key, value in map:
