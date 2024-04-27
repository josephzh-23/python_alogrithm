'''
So sto start off right here


Given a # x : x the max per store, how many stores would this require?

if # of stores < N: then x == a possible answer here

2 scenarios:
1) x = possible answer, then x + 1 also an answer, we want the min here

2) if x ！= possible answer, means use more than n stores, then x+ 1 not an answer
require same / more number of stores here
'''

'''
Same as koko eating banana here, you are trying to go 1 level above here 

'''


def minimizedMaximum(n: int, quantities) -> int:
    l, r = 0, 10 ** 6

    # as logn as < then the number of stores you are all good
    def good(x):
        count = 0
        # we have [11, 6]   and then 1 by 1,
        for cur in quantities:
            count += cur // x
            print("the count is ", count)
        return count <= n
    # O (m log R)
    while l < r:
        mid = (l + r) // 2


        # if the mid is good, we keep making the mid the new right and then
        # keep shrinking the window here
        if good(mid):
            r = mid

            # if not good
        else:
            l = mid + 1

    return l

minimizedMaximum(6, [11, 6])
