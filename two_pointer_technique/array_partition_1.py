

# This problem is called Array Partition 1
def arrayPairSum( nums):

    nums.sort()
    i=0
    sum =0

    while i < len(nums) -1:
        sum += nums[i]
        i+=2
    return sum

nums = [1, 2, 3, 5]
print(arrayPairSum(nums))