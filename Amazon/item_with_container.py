#
# # s = '|**|*|*'
#
# '''
# # integer array startIndices [1, 1]
# # integer array endIndices  [5, 6]
# [1, 5]
#
# '''
# def ans(s, startIndices, endIndices):
#
#     # used to keep track of number of items in between
#     length = 0
#
#
#     # check for open bracket
#     for c in s:
#         # means starting,  a new start
#         if c == '|' and length ==0:
#             length = 0
#
#         # case 2: length already sth  measn the end
#         elif c == '|' and length ==0:
#             # get the # of items here
