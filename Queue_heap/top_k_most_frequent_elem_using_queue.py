import heapq


h = heapq
def topKFrequent(nums, k):

    # we will be pushign into this ans = []
    ans = []
    freq = dict()

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    '''
    key here is the number, and value is the number of occurences 
        python heqp will rearrange and make sure that 
        the one with the least occurence be at the top 
    '''
    for number, occurence in freq.items():
        if len(ans) < k:
            # print(occurence)
            h.heappush(ans, [occurence, number])


        else:
            # print(occurence, number)
            # this not only adds but also removes
            itemRemoved = h.heappushpop(ans, [occurence, number])
            print("item removed is ", itemRemoved)
    # this only returns the key for the key
    # return [key for value, key in ans]

    return [key for value, key in ans]


num = [1, 2, 3, 4, 4, 4, 5]
res = topKFrequent(num, 1)
print(res)
# for key, val in res.items():
#     print('answer is', val)


