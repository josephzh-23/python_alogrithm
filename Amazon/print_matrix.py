import bisect

from collections import deque, defaultdict
from typing import List

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def findFirstBeautifulMoment(n, m, k, paint):

    dict = defaultdict(set)
    currentSameConsecutiveRowElem = 0
    currentSameConsecutiveColElem = 0
    for i, p in enumerate(paint):
        x, y = p
        dict[x].add(y)
        indexToLeft, indexToRight = y -1, y + 1
        if 1 <= indexToLeft and indexToLeft in dict[x]:
            currentSameConsecutiveRowElem+=1
        if indexToRight <= m and indexToRight in dict[x]:
            currentSameConsecutiveRowElem += 1

        dict[y].add(x)
        indexToTop, indexToBottom = x - 1, x + 1
        if 1 <= indexToTop and indexToTop in dict[y]:
            currentSameConsecutiveColElem+=1
        if indexToBottom <= n and indexToBottom in dict[y]:
            currentSameConsecutiveColElem += 1
        print(dict)
        print('this is', currentSameConsecutiveColElem, currentSameConsecutiveRowElem)
        if currentSameConsecutiveRowElem >= k and currentSameConsecutiveColElem >= k:
            print('the final answer', i)

n = 2
m = 3
k = 2 ; paint = [[1, 2], [2, 3], [2, 1], [1, 3], [2, 2], [1, 1]]
findFirstBeautifulMoment(n, m, k, paint)
