'''
When to use this one code here

Get the # of people alive during that year here so here we get
Logs[i] = [birth, death]
The population of some year x is the number of people alive during that year.

Input
logs = [[1993,1999],[2000,2010]]
Return:



This is a clasic sweep line algorithm.

Get all births and deaths in sorted array/map;
Now if its a birth, then increment and if its a death then decrement;
And keep count of the population while doing so. Result is the max population.

Sort first here

Population array : the axis here

'''
from typing import List


'''
What would this then beome

'''
def maximumPopulation(logs: List[List[int]]) -> int:
    dates = []
    for birth, death in logs:
        dates.append((birth, 1))
        dates.append((death, -1))

    dates.sort()
    # [(1993, 1), (1999, -1), (2000, 1), (2010, -1)]

    # and that's the answer here
    print("dates are ", dates)
    population = max_population = max_year = 0
    for year, change in dates:
        population += change
        if population > max_population:
            max_population = population
            max_year = year

    return max_year
logs = [[1993,1999],[2000,2010]]
maximumPopulation(logs)