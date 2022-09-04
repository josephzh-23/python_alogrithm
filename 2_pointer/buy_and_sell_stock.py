from typing import List


def maxProfit(self, prices: List[int]) -> int:
    l, r = 0, 1 # left = buy, right = sell

    while r < len(prices):
        # profitable
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)

            # shift our left pointer all the way until it's
            # at the right
        else:
            l = r
        r += 1

