
prices = [7, 1, 5, 3, 6, 4]

def buyAndSellStock(arr):

    max = 0
    # Buy first before you sell

    l, r= 0, len(arr) -1

    # store the max here
    max = max(max, arr[r] - arr[l])