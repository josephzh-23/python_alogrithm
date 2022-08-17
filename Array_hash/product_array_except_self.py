
# Basically we want to build this using the best solution possible

'''
Ex
        [1 ,2 ,3 , 4]       ->      [24, 12, 8, 6]
leftProd    [1, 1, 2, 6]
Start from the left, 1 since no value to the left of 1
1 = 1x1         2 = 2* 1        6 = 3*2
 leftProd[i] = leftProd[i-1] * leftProd[i-2]
rightProd   [24, 12, 4, 1]
start from the end, 1 since no val to right of 4
4= 4 *1         12 = 3* 4

output = [left Prod] * [right Product] = [24, 12, 8, 6]
'''

def productExceptSelf(nums):

    n = len(nums)

    leftProd = [0] *n
    rightProd = [0] * n
    outputArr = [0] *n

    leftProd[0] = 1
    rightProd[n-1] = 1

    for i in range(1,n):
        leftProd[i] = nums[i-1] * leftProd[i-1]