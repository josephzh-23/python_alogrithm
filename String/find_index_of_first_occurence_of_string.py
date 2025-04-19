

'''
s -> 0

'''
from collections import Counter

'''
Obtain both the haystack and needle 

These are very important here: 
n- m + 1 

we take a substring of haystack starting from the current index i and spanning m characters (the entire length of needle). In Python, the substring operation is haystack[i : i + m].

The followign is key here:
for i in range(n - m + 1):
    if haystack[i : i + m] == needle:
        return i
return -1

 O((n - m + 1) * m) is the solution that we have here 
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Length of the haystack and needle strings
        haystack_length, needle_length = len(haystack), len(needle)

        # Check all possible starting positions of needle in haystack
        for start in range(haystack_length - needle_length + 1):
            # If the substring matching the needle's length equals the needle, return the start index
            if haystack[start: start + needle_length] == needle:
                return start

        # If the needle is not found in haystack, return -1
        return -1