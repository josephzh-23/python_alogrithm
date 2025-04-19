'''

Define a set of servers
minimum availability

Consider the set of servers

 A client wants to choose a set of servers to deploy their application.

What's stability?
The client defines

stability of a set of servers =
min(availability amongst the servers) * sum(reliabilities of all the servers)

where the availabilityli] and reliabilityli] represent the availability and reliability factors of the ith server, find the maximum possible stability of any subset of servers.


Output:
find the maximum possible stability of among all non-empty subsetss


where availability = [1, 1, 3] and reliability = [1, 2, 2]
The possible subsets of servers are:

Case 1:
If just looking at one server
Indices => Stability
[0] => only 0th server => 1 * 1 = 1
[1] => only 1st server => 1 * 2 = 2
[2] => only 2nd server => 3 * 2 = 6


If we look at multipe servers and its subsets
[0, 1] => min(1, 1) * (1 + 2) = 3
[0, 2] => min(1, 3) * (1 + 2) = 3
[1, 2] => min(1, 3) * (2 + 2) = 4
[0, 1, 2] => min(1, 1, 3) * (1 + 2 + 2) = 5

The answer above is 6
'''
def solutions(reliability, availability, n):
    sorted_indices = sorted(range(n), key=lambda x: availability[x], reverse=True)

    '''
    The above sorts by availabilities, with the indices
    [1, 1, 3] -> [2, 0, 1]
    '''

    sorted_reliability = [reliability[i] for i in sorted_indices]

    '''
    Calculated the reliability for the sorted index
    Basically here we then get a situatino where we have the reliabity that corresponds to the 
    availaibility indice
    which becomes [2, 1, 2]
    '''

    '''
    Done with a prefix sum here 
    '''
    reliabilitySum = [r for r in sorted_reliability]

    for i in range(1, n):
        reliabilitySum[i] += reliabilitySum[i - 1]
    print(reliabilitySum)
    '''
    Calculate the max stability 
    '''
    max_stability = 0
    for i in range(n):
        stability = availability[sorted_indices[i]] * reliabilitySum[i]
        max_stability = max(max_stability, stability)

    print('the max is', max_stability)
solutions([1, 2, 2], [1, 1, 3], 3)