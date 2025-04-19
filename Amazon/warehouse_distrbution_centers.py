


'''



'''

def dfs(houses, start, k, prevMailbox, cache):

    if (k == 0):

        sum = 0

        '''
        No more mail boxes left 
     we need to return sum of distances from previous mailbox to each house without mailbox assigned
		
        '''
        for i in range(prevMailbox, len(houses)):
            sum += houses[i] - houses[prevMailbox]

        return sum


    if cache[start][k] != -1:
        return cache[start][k]

    