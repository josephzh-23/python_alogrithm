import heapq

h = heapq

def findKthLargest(nums, k):
    '''
    1, 2, 3, 4, 5
    '''

    minHeap =[]
    h.heapify(minHeap)

    # add everythign to it first
    for num in nums:
        h.heappush(minHeap, num)
        if len(minHeap) > k:
            element = h.heappop(minHeap)
            print(element)

    return h.heappop(minHeap)
nums = [1,2, 3,4, 5]
print(findKthLargest(nums, 4))

# most frequent element
'''
    
'''
def topKFrequent(nums, k):
    ans = []
    freq = dict()

    # when you go thru it
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] +=1


    # now push a pair

