'''
Using the dictionary approach here


'''
from collections import defaultdict, Counter


def majorityElements(nums):
    n = len(nums)
    times = n / 3
    res = []
    count = 0
    dict = Counter()
    for i, c in enumerate(nums):
        dict[c] += 1
        if dict[c] > n/3:

            res.append(c)
    print(res)

nums = [3, 2, 3]
majorityElements(nums)













