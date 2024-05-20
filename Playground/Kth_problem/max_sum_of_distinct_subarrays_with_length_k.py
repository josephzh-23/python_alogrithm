'''
And then here we have the code
- Len of subarray === k
- All the elements of the subarray are distinct. (set)


- we want the max ehre


This is a prefix sum problem

This can be done using the maximum of what you ahve here and then
'''


def maximumSubarraySum( nums, k):
    s = set()
    sum = 0
    maxi = 0
    l, r , cursum = 0, 0, 0
    for i in range(len(nums)):
        if (r - l) < k:
            n = nums[i]

            if n not in s:
                s.add(n)
                cursum += n
            r+=1
        else:
            l+=1
        maxi = max(cursum, maxi)
    print(maxi)

maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3)