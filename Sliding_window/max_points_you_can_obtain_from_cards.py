'''
choose cards from the beginning or end of the array in such a way that
 the sum of the remaining cards is minimized.

Let's look at two different choices of
K cards.

1st choices: will be to takeL cards from the left and
K−L cards from the right


2nd choice: tka l-1 cards from left and k-l + 1 card from right

Instead of recalculating the sum for the second choice, we can adjust the sum from the first choice to be the second
choice. We can notice that the difference between these two choices is that we added a card on the right side and we
removed a card from the left side.

So basically
 1. A simple way to implement this with two pointers is to start with picking all
K cards on the left.

 2. for each transition, remove 1 card on the left and add 1 card on the right
'''
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        # we have a left sum and then a right sum here
        leftSum = 0
        for i in range(k):  # calculate sum where all cards on the left side
            leftSum += cardPoints[i]
        rightSum = 0
        rightIndex = n  # pointer for the right cards
        ans = leftSum
        for leftIndex in range(k - 1, -1, -1):  # pointer for the left cards
            leftSum -= cardPoints[leftIndex]  # transition between choices
            rightIndex -= 1
            rightSum += cardPoints[rightIndex]
            ans = max(ans, leftSum + rightSum)
        return ans










