"""
T (n) = O (nlogn) + O(nlogn) + n = O(nlogn)

s (n) = 2n = O (n) from using sort
"""
def areAnagrams(s1, s2):

    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)