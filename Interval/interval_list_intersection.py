'''

firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
 Each list of intervals is pairwise disjoint and in sorted order.

[1, 3] and [2, 3] -> [1, 3]

Input: firstList = [[0,2],[5,10],[13,23],[24,25]],
secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


The logic for above is that when you have

[1, 3] and [2, 4] then the code becomes
[2, 3] above as said        it's the overlapped part

'''
from typing import List


def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    ans = []
    i = j = 0

    while i < len(A) and j < len(B):
        # Let's check if A[i] intersects B[j].
        # lo - the startpoint of the intersection
        # hi - the endpoint of the intersection
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])
        if lo <= hi:
            ans.append([lo, hi])

        # if first end < the 2nd end, skip list 1
        if A[i][1] < B[j][1]:
            i += 1

        # if 2nd end < 1st end, skip list 0
        else:
            j += 1

    return ans