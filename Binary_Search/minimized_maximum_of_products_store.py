# '''
# So sto start off right here
#
#
# Given a # x : x the max per store, how many stores would this require?
#
# if # of stores < N: then x == a possible answer here
#
# 2 scenarios:
# 1) x = possible answer, then x + 1 also an answer, we want the min here
#
# 2) if x ！= possible answer, means use more than n stores, then x- 1 not an answer
# require same / more number of stores here
# '''
#
# def minimizedMaximum(n: int, quantities)-> int:
#
#     l, r = 0, 10 **6
#
#     # as logn as < then the number of stores you are all good
#     def good(x):
#         count = 0
#         # we have [11, 6]   and then 1 by 1,
#         for cur in quantities:
#             count += (cur + x -1 ) //x
#
#             return count <=n
#
#     while l < r:
#         mid = (l + r)//2
#
#         if good(mid):
#             r = mid
#         else: