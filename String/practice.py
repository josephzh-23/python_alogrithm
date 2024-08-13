
'''
# abcdabbdds
   l
      r
'''
def longestSubstringWithoutRepeatingChar(s):

    l, r = 0, 0
    dict = set()
    maxlen = 0

    # use the 2 pter approach again
    for c in s:
        # make sure to remove it
        while c in dict:
            dict.remove(c)
            l+=1

        dict.add(c)
        r+= 1

        maxlen = max(maxlen, r-l + 1)

    return maxlen
s = "cooolabcdefghi"
print(longestSubstringWithoutRepeatingChar(s))

