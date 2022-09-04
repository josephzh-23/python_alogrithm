

'''
Notice there r a few scenarios
The brute force     (not good approach)
1. would be to sort each word inside  O (m * n log (n))

the better approach
2. would be to use the hash map scenario where O (m * n *26)

3. And then that's it
1. We want
    'a' -> 0
    'b' -> 1
    'z'-> 25
'''
import collections
from email.policy import default

from String_Array.findMode import List


def groupAnagrams(strs):
    res = collections.defaultdict(list) # mapping charCount to list of anagrams
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)

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


# def groupAnagrams(strs):
#     alpha = [0] *26
#
#     groupings = dict()
#     for word in strs:
#
#         '''
#         Step 1
#          use these "codes" to create groups
#         these "codes" are keys that will be used to index our hashmap on
#         for each word in input array
#         '''
#         code = convert(word)
#         print(' the code is ', code)
#         '''
#         Step 2 : instantiate hashmap (dictionary in python)
#         see if code matches any existing codes,
#             if not existing code, then create a new entry already
#         '''
#         if code in groupings:
#             groupings[code].append(word)
#         else:
#             # this will be a list of list as explained
#             groupings[code] = [word]
#
#
#     # this will return list[list]
#     return groupings.values()
#
#
# def convert(w):
#     alphabet = [0] *26
#     for letter in w:
#         index = ord(letter) - ord('a')
#         alphabet[index] += 1
#
#         return tuple(alphabet)

test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum']


res = groupAnagrams(test_list)
for l in res:
    print(l)



















strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
