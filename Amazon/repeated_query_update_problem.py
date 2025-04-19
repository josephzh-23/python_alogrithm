'''



The team at AWS Glue is developing on a new solution for frequent updates and computations of existing data. There are n data points where the ith data point is denoted by data[i]. There are q different updates to be made to the data where the jth update is denoted by query[j]. Each query consists of two integers denoted by query[j]
[0] and query[j][1].

For each jth query, perform the following:
• For all indices i, where data[i] = query[j][0], data[i] was changed to query[j][1](0≤j<q, O≤i<
n)
• Find the sum of all the integers in the array data.
• Persist the updates in the array.


Given an integer array data and a 2D integer array query, find the sum of all the data points after processing each query.

Input:

'''

from collections import defaultdict



'''
Frequency Map (freq_map):

The frequency map helps track how many times each value appears in data. This allows us to quickly determine if a value needs to be updated and how many times it appears.
Sum (total_sum):

We maintain a running total of the sum of data to avoid recomputing it from scratch after each query. Instead, after each query, we adjust the sum based on the update:
Subtract the contribution of the old value (how many times it appeared multiplied by the old value).
Add the contribution of the new value (how many times it appears multiplied by the new value).
Query Processing:

For each query, if the old value and new value are different, we update the frequency map and adjust the sum based on how many times the old value appears.
After processing each query, the updated sum is added to the result list.

n = 5
data = [2, 3, 4, 5, 6]
q = 3
query = [[2, 3], [2, 4], [4, 10]]

So freq[2] = 1

Process the old query here 

1. 
'''

def process_queries(data, query):
    # Step 1: Initialize frequency map and sum of the array
    freq_map = defaultdict(int)
    total_sum = sum(data)

    # Populate the frequency map
    for num in data:
        freq_map[num] += 1

    result = []

    # Step 2: Process each query
    for old_val, new_val in query:
        '''
        oldCount = 1
        oldVal = 2
        newVal = 3 
        freqMap[2] -= 1 = 0 
        freqMap[3] +=1  = 1 
        
        totalSum -= 1 * 2
        totalSum += 1 * 2
        
        And that's it for the total above here 
        '''
        if old_val != new_val:
            # Only proceed if the values are different
            count_old = freq_map[old_val]
            if count_old > 0:
                # Update the frequency map
                freq_map[old_val] -= count_old
                freq_map[new_val] += count_old

                # Adjust the total sum
                total_sum -= count_old * old_val
                total_sum += count_old * new_val

        # Store the current sum after this query
        result.append(total_sum)

    return result


# Example usage
data = [6, 2, 4, 6, 8, 10, 12, 5, 2]
query = [[2, 3], [5, 6], [8, 2], [4, 5], [6, 9]]


def repeatedQueryUpdateBruteForceApproach(data, query):
    res = []

    for q in query:
        oldVal, newVal = q

        # update the data based on above here
        for i in range(len(data)):
            if data[i] == oldVal:
                data[i] = newVal

        # after the update find hte sum here the above would work here very good !
    res.append(sum(data))
