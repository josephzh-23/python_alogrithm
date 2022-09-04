'''
 this is a very difficult problem, but to make it work, we
had to do some additional stuff


The 2d array as shown below:
water   0  0  1  0  1  2   1   0   0  1  0   0
stored

Pointer L  L  L  L  L  L   L   L   R  R  R   R
input   0  1  0  2  1  0   1   3   2  1  2   1

height(i) = what the input is
water(i) =  max( maxL, maxR) - height(i)

But just follow the code below
'''
from String_Array.findMode import List


'''
TC: O (n)
SC: O (1) because using 2 pter apporach no memory wasted here 
'''

def trap(height:List[int]) -> int:
    if not height: return 0

    l, r = 0, len(height) -1
    leftMax, rightMax = height[l], height[r]

    res = 0
    while l < r:
        if leftMax < rightMax:
            l+=1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r-=1
            rightMax = max(rightMax, height[r])
            res+= rightMax - height[r]
        return res