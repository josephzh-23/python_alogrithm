package Array

/*
Uisn gthe 2 pointer apporach here
Notice here that the as long as rightMax[i] > leftMax[i] from
elem 0 -6, the water trapped depends upon the left_max

As long as left_max[i]>right_max[i] (from element 8 to 11).
water depends on the right max here

while left < right do:
    if height(left] < height[rihgt]:
        if height[left] > leftMax update leftMax
        else: add leftMax - height[left] to answer

 */