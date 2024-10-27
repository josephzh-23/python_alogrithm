'''


Within days days

Ith package has a weights[i] <  maximum weight capacity of the ship

Least weigth capacity so everything shipped within days

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Shipping maximum capacity within d days here
'''
from typing import List


def shipWithinDays(weights: List[int], days: int) -> int:
    '''
    The lower bound is at least the maximum of each

    The maximum bound is the maximum of the weights here
    '''
    l = max(weights)
    r = sum(weights)

    def shipDays(shipCapacity: int) -> int:
        days = 1

        '''
        
        Capacity + weight > shipCapacity here 
        
        capacity is what's left of the previous day, that couldn't go in 
        '''
        capacity = 0
        for weight in weights:
            if capacity + weight > shipCapacity:
                days += 1
                capacity = weight

                print("capacity is ", capacity)
            else:
                capacity += weight
        return days

    while l < r:
        m = (l + r) // 2
        if shipDays(m) <= days:
            r = m
        else:
            l = m + 1

    return l

weights = [1,2,3,4,5,6,7,8,9,10]; days = 5
shipWithinDays(weights, days)