from typing import List


'''
And above is what you are looking at here 

Input: strs = ["flower","flow","flight"]
Output: "fl"

the above give you what you are looking for here 
'''

def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        '''
        Until we find it we will keep going at this 
        '''
        while strs[i].find(prefix) != 0:
            '''
            We basically keep cutting this down until we get to the prefix here fl 
            '''
            prefix = prefix[0: len(prefix) - 1]
            print("prefix is", prefix)
            if prefix == "":
                return ""
    return prefix
strs = ["flower","flow","flight"]
longestCommonPrefix(strs)