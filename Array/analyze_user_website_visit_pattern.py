'''
User history:
map of various pages that the user has visited:

The hashmap is of type {user: [pages]}

And this is a very good question here,

'''
from collections import defaultdict
from itertools import combinations
from typing import List


def mostVisitedPattern(username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    # zip the time, user and website to one list
    tuw = list(zip(timestamp, username, website))

    # we need to sort them by time --> username --> website
    sorted_tuw = sorted(tuw)

    # We will polulate a user history hashmap of various websites visited. The hashmap is of type {user: [websites]}
    user_history = defaultdict(list)
    for t, u, w in sorted_tuw:
        user_history[u].append(w)

    # get various combinations possible for various users
    patternCount = defaultdict(int)
    for user, websites in user_history.items():

        # get various combinations possible for various users in the pair of 3 and add them to set so that they are unique
        '''
        What this gives is basically the code 
        ['home', 'cart', 'maps', 'home']
         {('home', 'cart', 'home'), 
         ('home', 'cart', 'maps'), 
         ('home', 'maps', 'home'), 
        ('cart', 'maps', 'home')}
        
        '''
        userCombinations = set(combinations(websites, 3))
        print('the websites are ', websites, userCombinations)

        # for every pair of userCombination, we will update the count. This count will make sense for second user onwards having the same pattern
        for userCombination in userCombinations:
            patternCount[userCombination] += 1



    #then comes the part where we have to sort both the pattern key lexiographically
    # and the count lexiographically from min to the max here as well
    # now whe sorting is done here and we are good to go and that's pretty good

    # already as it is

    '''
    
    '''
    maxpattern, maxcount = '', 0
    for pattern, count in patternCount.items():

        # this is how we make sure that the pattern is sorted by using the <
        # comparator here
        if count > maxcount or (count ==maxcount and pattern < maxpattern):
            maxpattern = pattern
            maxcount = count

    print("max pattern", maxpattern)
    return maxpattern
usernames = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
websites = ["home","about","career","home","cart","maps","home","home","about","career"]
mostVisitedPattern(usernames, timestamp, websites)