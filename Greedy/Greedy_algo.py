'''

n gas stations
n costs to go from 1 to the next

Given two integer arrays gas and cost, return the starting gas station's index if you can travel
 around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.


As we traverse the stations, we maintain a running total of the net gas difference between the available gas and the cost of traveling.


gas      [1, 2, 3, 4, 5]
cost.    [3, 4, 5, 1, 2]
diff     [-2, -2,-2, 3, 3]

During the iteration, if the net gas difference total at any point becomes negative, it indicates that the current starting station cannot complete the circuit.

In such cases, we reset the total to zero and
update the starting index res to the next station. This step allows us to explore alternative starting points,
 as the current one fails to sustain the journey due to insufficient gas.



'''
from typing import List



def canCompleteCircuit( gas: List[int], cost: List[int]) -> int:
    # Check if the total gas available is less than the total cost of traveling
    if sum(gas) < sum(cost):
        return -1

    total = 0  # Initialize the net gas difference
    res = 0  # Initialize the starting index

    # Iterate through the gas stations
    for i in range(len(gas)):
        # Update the net gas difference
        total += (gas[i] - cost[i])

        # If the net gas difference becomes negative, reset to zero and update the starting index
        if total < 0:
            total = 0
            res = i + 1

    return res

gas = [1,2,3,4,5]; cost = [3,4,5,1,2]
print(canCompleteCircuit(gas, cost))


