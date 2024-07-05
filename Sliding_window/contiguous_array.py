'''


Here using the map version of this first and see how this works
How does this work?

if running count already in the hashmap, then already found a hashmap where
diff between 0 and 1 is the same as previous index

Equal # of 0 and 1 in between 2 indices here

'''
def finalSolution(nums):

    # create a hashmap first and then
    s = 0
    ans = 0
    #store the max length of this
    mp = {0: -1 } #to start off

    ans = 0

    for i, n in enumerate(nums):
        if n == 1:
            s +=1
        else:
            s -=1


    # check if running count already here
        if s in mp:
            '''
            Then compute the distance from the first i - mp[s] # the first time this was encounterd 
            until this point here which is what we need now 
            '''

            ans = max(ans, i - mp[s])

        # update the index here
        else:
            mp[s] = i

    # and that's the final answre here
    return ans












