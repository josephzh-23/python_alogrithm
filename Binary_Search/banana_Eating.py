

'''

3 key points here

0.     l, r = 1, max(piles)     this is important
1.  for p in piles:
        hours += math.ceil(p/k)
2.      if hours<= h:
            res = min(res, k)
            r= k-1


The process is as belows
1. ith pile has pile[i]

pile has < k bananas,  len(p) <= h,

[1, 1, 2, 2, 3] 		h = 5,

The minimum h in there is 5, because you need 1 hour for each pile.

Example:
[3, 6, 7, 11] 		h = 8

- k = 1 min	what’s the max here? if k =11, we can eat 11 in 1 hour,
The approach is to go from  k = [1…. 11] and find that 1 number in between, where we can finish everything in between

The time complexity O (P* log(max(P))
- the improved time complexity here


Use the binary search here
Ex:   [1,   2,  3,  4,  5,  6,  7,  8 , 9,  10, 11]
1. [3, 6, 7, 11] 	if k = 6	(the middle number)

3/6 + 6/6  + 7/6 + 11/6 = 1 + 1 + 2 + 2 = 6

    6 < 8
    but you can try even the smaller value as well, which means
    r= k-1

2.

h = 8       the time she has to eat
30 -
Eat at speed of K, if f the pile has less than k bananas,
she eats all of them instead and
 will not eat any more bananas during this hour.

 Return the minimum integer k such that she can eat all the bananas within h hours.
'''
import math
from typing import List


def kokoEatBanana( piles: List[int], h: int)->int:

    l, r = 1, max(piles)
    res = r
    while l<=r:
        k = (l + r)//2

        hours = 0
        for p in piles:
            hours += math.ceil(p/k)

        if hours<= h:
            print('why need res', res)
            res = min(res, k)
            r= k-1

        # greater than the h given
        else:
            l = k+1

    return res

res = [30,11,23,4,20]
result = kokoEatBanana(res,6 )
print(result)