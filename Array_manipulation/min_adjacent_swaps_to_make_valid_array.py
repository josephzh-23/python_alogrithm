

# and then here we have the code and then there we have the code

'''

ou are given a 0-indexed integer array nums.

Swaps of adjacent elements are able to be performed on nums.

A valid array meets the following conditions:

The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.
Return the minimum swaps required to make nums a valid array.


Input: nums = [3,4,5,5,3,1]
Output: 6

We need to find the index of left most min value and index of right most max value.
Then count the number of swaps needed to put them at the extreme of the array.

Steps:
1. find the index of left most min value and right most max value here
2. Cal # of swaps required to push the min to the 0th indx and max to the n-1 index here

3. the calculation: minValIndex + ((arraySize - 1) - maxValIndex)

4. The edge case where the maxValIdx < minIndex here, thenw
minValIndex + ((arraysize-1) - maxValIndex) - 1.

And this is the 2nd case here: and that's it
and the 2nd case where maxVal
 minValIndex + ((arraysize-1) - maxValIndex)

And that's it here we have a lot to get to today here 
'''

def minSwaps(nums):
    n = len(nums)

    if (n==1):
        return 0

    maxInd, minIdn, maxVal = -1, -1, -1
    minVal = float("-inf")
    numSwaps = 0
    for i in range(n):
        if(nums[i] >=maxVal):
            maxInd = i  ; maxVal = nums[i]

        if nums[i] < minVal:
            minInd = i, minVal = nums[i]

    '''
    There r 2 situations here 
    '''
    if minInd < maxInd:
        numSwaps = minInd + (n- maxInd - 1)

    else:
        numSwaps = n- maxInd -1
        numSwaps += minInd - 1

    return numSwaps



















