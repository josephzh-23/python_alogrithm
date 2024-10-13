'''

There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.
Return the total number of friend requests made.


Let's braek this down here

A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

age[y] <= 0.5 * age[x] + 7

Because to get to age[y] from here, u need mathmatical proof here

age[x] >= (age[y] - 7) *2   here in this case here


age[y] > age[x]
age[y] > 100 && age[x] < 100

'''
import bisect
from typing import List


def numFriendRequests(ages: List[int])-> int:
    ages.sort()
    n = len(ages)
    ans = 0
    '''
    ages = [16, 17, 18] 
    
    '''
    for idx, age in enumerate(ages):              # for each age
            lb = age                                  # lower bound
            ub = (age - 7) * 2                        # upper bound

            i = bisect.bisect_left(ages, lb)          # binary search lower bound
            j = bisect.bisect_left(ages, ub)          # binary search upper bound
            if j - i <= 0: continue
            ans += j - i                              # count number of potential friends
            print("lower, upper and age",
                 ans)
            if lb <= age < ub:                        # ignore itself
                print("i came here ")
                ans -= 1
    # and then the answer came here first 
    print("answer is ", ans)
ages = [16, 17, 18]
numFriendRequests(ages)