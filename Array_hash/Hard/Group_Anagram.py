

'''
Notice there r a few scenarios
The brute force     (not good approach)
1. would be to sort each word inside  O (m * n log (n))

the better approach
2. would be to use the hash map scenario where O (m * n *26)

3. And then that's it


'''
import collections
from email.policy import default

from Array_hash.findMode import List


def groupAnagrams(strs):
    res = collections.defaultdict(list) # mapping charCount to list of anagrams

    '''
    key : [eat, tea...]
    '''
    for s in strs:
        count = [0] * 26    # a.... z
        for c in s:

            # map a to index 0,  map 'z' to index 26
            # and below is the way to achieve that
            count[ord(c) - ord('a')] += 1


            # this needs to be a tuple because list can't take key
        res[tuple(count)] = s
    return res.values()


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))