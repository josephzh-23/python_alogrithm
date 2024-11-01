
'''

Then we fill it up by updating it with birth year and end year.
For index of birth year we add 1 to represent birth
For index of death year we sub 1 to represent death
Then we move from left to right, get running/rolling population for each year and get the max one.

The smallest value from smallest year
Why does this work ? well as we are moving left to righ, the max value we get will always be from the smallest year
and its going to be from the input array. For years that are not in the input array,
 will be having the rolling window value of the previous index.
'''
from math import inf
from typing import List


def maximumPopulation( logs: List[List[int]]) -> int:
    # range of years
    start, end = inf, -inf

    for s, e in logs:
        start = min(start, s)
        end = max(end, e)

    # births = [0 for i in range(end - start + 1)]
    births = [0] * (end - start + 1)
    print('birth is', births)
    # now we mark all the births with + 1
    # we decrement all the deaths with -1
    for s, e in logs:
        sI = s - start
        eI = e - start
        # born
        births[sI] += 1
        # death
        births[eI] -= 1

    # at the beginnign the year is the lowest that you can have at the start 
    year = 0
    # iterate over the births and deaths timeline
    # we could have kept a runningWindow and maxPopulation variable
    # it would have worked in the same way as current val + previous val
    for index in range(1, len(births)):
        # we get the total population at this current year
        births[index] += births[index - 1]
        # if current year net is more than the max year, then we got a new max year
        if births[index] > births[year]:
            year = index

    return year + start
logs = [[1993,1999],[2000,2010]]

maximumPopulation(logs)