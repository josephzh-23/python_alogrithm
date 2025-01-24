import collections
from collections import defaultdict

# and then the above makes sense here
def groupStrings( strings):
    # A mapping from normalized string to the list of strings that match the pattern
    grouping_dict = collections.defaultdict(list)

    for st in strings:

        char_diffs = []
        i = 1
        while i  < len(st):
            # this helps deal with the rotation where you have za
            # because
            shift = (ord(st[i]) - ord(st[i - 1])) % 26
            i +=1
            char_diffs.append(shift)

        '''
        Your dictionary will look sth like the following here 
        as said interesting 
        '''
        grouping_dict[tuple(char_diffs)].append(st)
    print(grouping_dict)
# so these
groupStrings(["xyz", 'abc'])