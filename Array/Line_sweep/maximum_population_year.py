'''


What does this algo do here? This is very important here

logs = [[1993,1999],[2000,2010]]


    Scan from left and accumulate the population, everytime check if current population is greater
than global max , if yes update population count and year both.
This scanning from left to right is line sweep.
Time Complexity = O(n log n) (due to tree map) initiialization, iteration of map take O(n) time.


The above is what we have here, the start and the finish here
Return the earliest year with the maximum population.

This scanning from left to right is line sweep


'''
from typing import List


def solution(logs: List[List[int]]):

    population = 0
    for l in logs:
        # and then here you have the code











