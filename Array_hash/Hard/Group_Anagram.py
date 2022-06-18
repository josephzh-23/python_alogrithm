

'''
Notice there r a few scenarios
The brute force
1. would be to sort each word inside  O (m * n log (n))

the better approach
2. would be to use the hash map scenario where O (m * n *26)

3. And then that's it


'''
import collections

from Array_hash.findMode import List


def groupAnagrams(strs):
    ans = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)] = s
    return ans.values()


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(str))