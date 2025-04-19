import heapq


word = "w*ord"
print("wlord"==word)
nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
k = 2

'''
Doing this without the other solution
'''

def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # the will have freq[count] = [elem, elem, elem]
    '''
    The one with highest frequency will be at the back as said of the frequency
    '''
    for n, c in count.items():
        freq[c].append(n)

    print("frequency is ", freq)
    res = []
    # to go from the back of the array here
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            print("res is", res)
            if len(res) == k:
                return res
    print(count)


print(topKFrequent(nums, 1))
