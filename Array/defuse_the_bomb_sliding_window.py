'''

Working wiht a circular array here, and then


if k > 0, replace the ith number with sum of next k numbers
'''
def defuseBomb(arr, k):
    # Compute sum of first window of size k
    window_sum = sum(arr[:k])
    res = [0] * len(arr)
    n = len(arr)
    # Compute the sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # the current window.
    for i in range(n - k):
        res[i] += window_sum + arr[i]
        window_sum = window_sum - arr[i] + arr[i + k]
    print(res)

defuseBomb( arr= [5,7,1,4], k = 3)