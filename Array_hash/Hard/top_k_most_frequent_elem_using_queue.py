import heapq


h = heapq
def topKFrequent(nums, k):

    ans = []
    freq = dict()

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    for key, val in freq.items():
        if len(ans) < k:
            h.heappush(ans, [val, key])
        else:
            h.heappushpop(ans, [val, key])

    # this only returns the key
    return [key for value, key in ans]


num = [1, 2, 3, 4, 4, 4, 5]
res = topKFrequent(num, 1)
# for key, val in res.items():
#     print('answer is', val)


