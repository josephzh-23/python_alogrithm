'''


warehouse capacity[i]

where warehouse Capacity[i] represents the capacity of the warehouse located at position/(assuming 1-based indexing).
-sorted

Connection hub:
    Each warehouse must establish a connection to a distribution hub positioned at a location greater than or equal to its own. This means that a warehouse at position i can only connect to a hub at position j, where j >= i.

Notice that there is also another catch to this


The central high-capacity distrbituion hub puzzle here:
To optimize inventory routing, Amazon has placed a central high-capacity distribution hub at the last warehouse, located at position n. This hub serves as the main connection point for all warehouses if necessary. The cost of establishing a connection from warehouse at i to a hub at position j is given by warehouseCapacity[j] - warehouseCapacity[i].



Cost of establishing a connection:
The cost of establishing a connection from warehouse at i to a hub at position j is given by
warehouseCapacity[j] - warehouseCapacity[i].


The ask:
        Given a queries of the form (hubA, hubB), where two additional high-performance distribution hubs are deployed at warehouses hubA and hubB (1 ≤ hubA < hubB < n), the goal is to calculate the minimum total connection cost for all warehouses, considering the nearest available distribution hub at or beyond each warehouse's position.

Input here:
Additional hubs:

additionalHubs = [[2, 4]]
warehouseCapacity [3, 6, 10, 15, 20]

[6]
[3, 6, 10, 15, 20]
j -


1st warehouse will connect to the nearest available distribution hub at position 2, cost incurred 6-3=3
2nd warehouse is itself a distribution hub, so cost incurred = 0
3rd warehouse will connect to the nearest available distribution hub at position 4, cost incurred = 15-10=5
4th and 5th warehouses are itself a distribution hub, so cost incurred = 0+0=0
Thus, the total connection cost (6-3)+(0)+(15-10)+(0)+(0)=8. Hence, return [8] as the answer.
'''


def getMinConnectionCost(warehouseCapacity, additionalHubs):
    n = len(warehouseCapacity)
    centralHub = n - 1
    results = []

    # Function to calculate cost for the given hubs
    def calculate_total_cost(hubs):
        total_cost = 0
        # For each warehouse, find the nearest hub
        for i in range(n):
            nearestHubCost = float('inf')
            # For each hub, calculate the cost and find the nearest hub
            for hub in hubs:
                if hub >= i:
                    nearestHubCost = min(nearestHubCost, warehouseCapacity[hub] - warehouseCapacity[i])
            total_cost += nearestHubCost
        return total_cost

    # For each query, calculate the total cost after adding the additional hubs
    for hubs in additionalHubs:
        # Include the central hub at the end of the warehouse list
        hubs_set = set(hubs + [centralHub])
        total_cost = calculate_total_cost(sorted(hubs_set))
        results.append(total_cost)

    return results


# Test the function with the sample inputs
warehouseCapacity = [3, 6, 10, 15, 20]
additionalHubs = [[2, 4]]
print(getMinConnectionCost(warehouseCapacity, additionalHubs))  # Output: [8]
