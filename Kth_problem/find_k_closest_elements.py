'''

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
'''
from typing import List

'''
Time complexity: O(N⋅log(N)+k⋅log(k)).

To build sortedArr, we need to sort every element in the array by
 a new criteria: x - num. This costs O(N⋅log(N)). Then, we have to sort sortedArr again to get the output in ascending order. 

This costs O(k⋅log(k)) time since sortedArr.length is only k.

'''

def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

    # we can try Sort this first
    sorted_arr = sorted(arr, lambda num: abs(x - num))
    res = []
    for i in range(k):
        res.append(sorted_arr[i])

    return sorted(res)