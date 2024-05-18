'''
Given an integer array bloomDay, an integer m and an integer k.

We need to make m bouquets. To make a bouquet,
you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in
the bloomDay[i] and then can be used in exactly one bouquet. Return the minimum number of days you need to wait to be
able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.


Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

Need to wait 1 day, 2 days and then 3 days from this here


Brute force approach here
What's m here:  at least m # of boutiques containing k roses
1. If m*k > arr.size: This means we have insufficient flowers. So, it is impossible to make m bouquets and
 we will return -1.

2.where 'arr[i]'  denotes that the 'ith' rose will bloom on the 'arr[i]th' day.

3.
Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to min(arr[]) and the high will point to max(arr[]).
'''
# min days to wait until m bouquets can be made from the garden
def possible(arr, day, m, k):
    n = len(arr)  # size of the array
    cnt = 0
    noOfB = 0
    # count the number of bouquets
    for i in range(n):
        if arr[i] <= day:
            cnt += 1
        else:
            noOfB += cnt // k
            cnt = 0
    noOfB += cnt // k
    return noOfB >= m

def roseGarden(arr, k, m):
    val = m * k
    n = len(arr)  # size of the array
    if val > n:
        return -1  # impossible case
    # find maximum and minimum
    mini = float('inf')
    maxi = float('-inf')
    for i in range(n):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])

    # apply binary search
    low = mini
    high = maxi
    while low <= high:
        mid = (low + high) // 2
        if possible(arr, mid, m, k):
            high = mid - 1
        else:
            low = mid + 1
    return low

arr = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3
m = 2
ans = roseGarden(arr, k, m)
if ans == -1:
    print("We cannot make m bouquets.")
else:
    print("We can make bouquets on day", ans)

















