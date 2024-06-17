'''


You are given a list of songs where the ith song has a duration of time[i] seconds.

(time[i] + time[j]) % 60 == 0.

time = [30,20,150,100,40]

(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60


'''
from typing import List



'''
Below is the brute force approach here 


(a+b) % 60=0
       ⇓
((a % 60)+(b % 60)) % 60=0
'''


def solution(time):

    '''

    Next, we iterate through each song duration in time and calculate its remainder when divided by 60.

0. So basically being between count[(60 - t % 60) and count[t % 60] and that's it
2
1 we then look for other song durations with a remainder of (60 - t % 60) % 60

2.since this would result in a total duration that is divisible by 60.
3.
    '''
    #This array is used to keep track of the frequency of each
    # remainder value, which will be useful later when we want to find pairs that add up to 60.
    count = [0] * 60
    res = 0

    '''
    
    
    '''
    for t in time:
        res += count[(60 - t % 60) % 60]
        count[t % 60] += 1
    return res






def numPairsDivisibleBy60(self, time: List[int]) -> int:
    ret, n = 0, len(time)
    for i in range(n):
        # j starts with i+1 so that i is always to the left of j
        # to avoid repetitive counting
        for j in range(i + 1, n):
            ret += (time[i] + time[j]) % 60 == 0
    return ret