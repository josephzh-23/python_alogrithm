# top occuring element
'''
Strategy here
    use a hashmap [ frequency, element]
    Use  Then use a priority queue to store the element-frequency pair (Max-Heap).
     This gives the element which has maximum frequency at the root of the Priority Queue_practice
'''


# Now try implementing this

# Add items into the heap,
import heapq

''' Visualization here 
[[3, 1], [2, 2] , [1, 3] ]
Notice above we have the frequency and the elements here 
'''

def topKOccuringElements(arr, k):

    ans = []
    freq= {}

    for num in arr:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] +=1

    for key, val in freq.items():
        heapq.heappush(ans, [val, key])
        print('the pushed value is ', val, key)
        if len(ans) > k:
            heapq.heappop(ans)

    # this is basically list comprehension here
    return [key for value, key in ans]

arr = [1, 2, 3, 4, 5, 5]
print('the list is ', topKOccuringElements(arr, 2))