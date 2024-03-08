import heapq

nums = [1, 1, 1, 2, 2, 3]
k = 2

def mapWithCount(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n]= 1+ count.get(n, 0)

    print(count)
mapWithCount(nums, 2)











