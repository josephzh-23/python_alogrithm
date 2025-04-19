'''

Example Walkthrough

Let's walk through a small example based on the solution approach given above.

Consider we have spells = [15, 10], potions = [1, 5, 20, 8], and success = 120.

We aim to determine for each spell, how many potions > success
threshold when multiplied by the spell.

 Before: [1, 5, 20, 8] After Sort: [1, 5, 8, 20]

Using Binary Search: We then apply binary search to find the count of potions that can pair with a spell to achieve the success.

For spell 15: We search for the smallest potion that when multiplied is at least 120. That potion should be

120 / 15 = 8.


For spell 10: We need a potion of at least 120 / 10 = 12.
Calculating Successful Pairs:

For spell 15: Using bisect_left, we find the index where 8 could fit in the sorted potions array [1, 5, 8, 20], which is index 2, which points to the value 8 here
For spell 10: Using bisect_left, we find the index where 12 could fit, which is after 8 and before 20. Hence, the index would be 3, which points to between 8 and 20 here.


Storing Results:

For spell 15: m - index is 4 - 2 = 2. So, there are 2 successful potion combinations for the spell 15.
For spell 10: m - index is 4 - 3 = 1. Therefore, there is 1 successful potion combination for the spell 10.


Generating the Output: According to the steps described in the solution approach, we create a list with the counts of successful combinations for each spell. The result for our example will be [2, 1].

For better understanding, here's how the binary search part of the code would operate in a step-by-step manner:

Spell is 15: bisect_left([1, 5, 8, 20], 120/15)

It finds the position of 8 because 8 * 15 is exactly 120.

index = 2, total potions m = 4, successful combinations: 4 - 2 = 2.

Spell is 10: bisect_left([1, 5, 8, 20], 120/10)

It passes over 8 (since 8 * 10 is less than 120) and settles before 20.

index = 3, successful combinations: 4 - 3 = 1.

Thus, the final returned value for this particular example with the spells and potions given would be [2, 1]. Each spell has a corresponding count of potions that, when multiplied, meet or exceed the success threshol
-
'''
import bisect
from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:

    potions.sort()

    numPotions = len(potions)
    res = []
    for spell in spells:
        # we obtain the min potion that still meets the requirement
        index = bisect.bisect_left(potions, success/spell)
        res.append(numPotions - index)

    return res


spells = [5,1,3]; potions = [1,2,3,4,5]; success = 7
print(successfulPairs(spells, potions, success))

