import math

'''

 There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses 
some pile of bananas and eats k bananas from that pile

k the minimum eating speed here 
Return the minimum integer k 

'''
def minEatingSpeed(piles,h):

    l, r =1, 1
    r = max(piles)
    while l < r:
        '''
            // Get the middle index between left and right boundary indexes.
                // hourSpent stands for the total hour Koko spends.
        '''
        mid = (l + r) //2
        hourspent = 0

        # Iterate over the piles and calculate hour_spent.
        # We increase the hour_spent by ceil(pile / middle)
        for pile in piles:
            hourspent += math.ceil(pile / mid)

        # Check if middle is a workable speed, and cut the search space by half.
        if hourspent <= h:
            right = mid
        else:
            left = mid + 1

        # then we can update hte left and the right accordingly
        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
    return right






