

def maxProfit(prices):
    """
    Will have the 2 pointers one on the left and one on right
    both will be at left and right

    when arr[r] > arr[l]
        increase r only

    else:
        increase left and right here
  """

    l, r= 0, 1
    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]

            maxP = max(maxP, profit)
        else:
            l = r

        r+=1

    return maxP

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
