from collections import Counter


def maxSubarraySum(nums, k):
    numsCounter = Counter(nums[:k])
    #calculate the sum of first few elements here
    cursum = sum(nums[:k])

    # If the number of unique elements equals 'k', assign sum to 'max_sum', else 0
    max_sum = cursum if len(numsCounter) == k else 0
    for i in range(k, len(nums)):

        # first element in the window
        firstElem = nums[i - k]


        # This is the current elem
        num = nums[i]
        numsCounter[num] +=1
        cursum += num

        # remove the first elem from the window here
        # decrease the count of the element that slid out here
        numsCounter[firstElem] -=1
        cursum -= firstElem

        # If there's no more instances of the (i-k)'th element, remove it from the counter
        if numsCounter[nums[i - k]] == 0:
            del numsCounter[nums[i - k]]

        # Update 'max_sum' if the number of unique elements in the window equals 'k'
        if len(numsCounter) == k:
            max_sum = max(max_sum, cursum)
    # this is the starting point here
    return max_sum