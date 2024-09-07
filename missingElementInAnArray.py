# # binary search problem
#
# def missingElement(nums, k):
#     # how woudl this go ok?
#     i = 1
#     res = []
#     tempNum = nums[0]
#     while i < len(nums):
#         # 7, 9 , 10
#         while tempNum != nums[i]:
#             # the one to add here
#             res.append(tempNum)
#             tempNum+=1
#
#         i +=1
#     print(res)
#     return res[k]
#
# missingElement([4, 7, 9, 10], 1)