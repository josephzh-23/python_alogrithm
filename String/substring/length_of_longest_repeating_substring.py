

def lengthOfLongestSubstring(s):

    map = {}

    str = s

    for c in str:
        idx = ord(c) - ord('a')
        map = map.get(c, 0) + 1


