'''

For deleting now, how would this work?

Remove 3 is better than remove 2 elements




1. we r talking 3, 6, 9, 12 and then
When count ==3 , it will take us count /3 to remvove all the elements here

2. Where you have more than 1 here
4, 7, 10, 13 here


Case 2:
In such case, eliminate the 2 pairs here

    * count = 4
    4 - 2 - 2 = 0 -> eliminate two pairs
    operations required = 2
    * count = 7
    7 - 2 - 2 = 3 -> eliminate two pairs
    3 - 3 = 0 -> eliminate remaining triplets
    operations required = 3

 -
 Case 3:
 * count = 5
    5 - 2 = 3 -> eliminate one pair
    3 - 3 = 0 -> eliminate remaining triplets
    operations required = 2
* count = 8
    8 - 2 = 6 -> eliminate one pair
    6 - 3 - 3 = 0 -> eliminate remaining triplets
    operations required = 3
* count = 11
    11 - 2 = 9 -> eliminate one pair
    9 - 3 - 3 - 3 = 0 -> eliminate remaining triplets
    operations required = 4



Based on above the # of operations required to remove a total of count
=
ceil(count/3)
# create
'''
from collections import Counter
from math import ceil
from typing import List


def minOperations(self, nums: List[int]) -> int:
    counter = Counter(nums)
    ans = 0
    for c in counter.values():
        if c == 1:
            return -1
        ans += ceil(c / 3)
    return ans