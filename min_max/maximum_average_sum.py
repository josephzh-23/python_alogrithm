# this is the basis of the maximum average problem here and then more
# stuff that's needed
nums = [1, 2, -5, -6, 50, 3]
curAvg = 0
curSum = 0
i, j = 0, 0


def findMaxAverage(nums, k):
    sum, i = 0, 0
    for i in range(k):
        sum += nums[i]

    maxsum = sum
    startindex = 0

    endindex = k

    while (endindex < len(nums)):
        sum -= nums[startindex]  # remove previous element
        startindex += 1
        sum += nums[endindex]  # add the next element
        endindex += 1

        maxsum = max(maxsum, sum)

    return float(maxsum/ k)
