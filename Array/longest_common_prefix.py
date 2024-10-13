from typing import List


'''
And above is what you are looking at here 

Input: strs = ["flower","flow","flight"]
Output: "fl"

the above give you what you are looking for here 
'''

def longestCommonPrefix(strings: List[str]) -> str:
    if len(strings) == 0:
        return ""
    # the outer loop goes thru each char of the first string on the outside
    for index in range(len(strings[0])):
        for string in strings[1:]:
            # check if we have reached the edn here
            # or a character mismatch is found
            if index >= len(string) or string[index] != strings[0][index]:
                return strings[0][:index]
    # If no early return happened, the first string itself is the common prefix
    return strings[0]
                # return the longest prefix we have found so far here
    # and then when we keep going here and then the code will become


