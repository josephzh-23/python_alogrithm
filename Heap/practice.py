import heapq

h = heapq



'''

1, 2, 3, 4, 
1 will be at the front 

'''
def findKthSmallest(arr, k):

    ans = []
    i = 0
    for num in arr:
        if len(ans) > k:
            h.heappush(ans, num)
        else:
            val = h.heappop(ans)
            print(val)

    return h.heappop(ans)

arr = [1, 2, 3, 4, 5]
print(findKthLargest(arr, 2))


# will come back to this


def topKMostFreq(nums, n, k):
    ans = []
    freq = dict()

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1



    for num, occurence in dict.items():
        if len(ans) < k:
            h.heappush(ans, [num, occurence])

        else:
            h.heappop(ans)