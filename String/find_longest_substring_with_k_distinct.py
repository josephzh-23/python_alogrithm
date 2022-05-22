

"""
Video: Coding Simplified
"aabbcc", k = 1
Max substring can be any one from {"aa" , "bb" , "cc"}.

"aabbcc", k = 2
Max substring can be any one from {"aabb" , "bbcc"}.

"aabbcc", k = 3
There are substrings with exactly 3 unique characters
{"aabbcc" , "abbcc" , "aabbc" , "abbc" }
Max is "aabbcc" with length 6.
"""


'''
    Pseudo code 
    iterate thru whole loop, build a dictionary of [char, # of char]
    using i
        while len(map) > k:
            Start decrementing the count in dictionary for a char
            that already exists
            update j
            
            check which the count for which key no longer exists 
'''
def findLongestSubstringWithKDistinctChar(str, k):

    if not str or len(str)==0 or k<=0 or k>len(str):
        return

    maxl = 0
    i, j = 0, 0

    # map would have {key, count} values here

    map = {}

    while j < len(str):

        cur = str[j]
        # put each char into the map first

        map[cur] = map.get(cur, 0) + 1

        # we will iterate thru map
        # the length of map will always be < k
        while len(map) > k:
            charFromFront = str[i]

            # Start decrementing the count in dictionary for a value
            # that already exists
            map[charFromFront] = map.get(charFromFront) -1

            if map.get(charFromFront) ==0:
                del map[charFromFront]
            i+=1

        # Then update the max length
        maxl = max(j - i + 1, maxl)
        j+=1

    return maxl

maxl = findLongestSubstringWithKDistinctChar("joosephhhhkjjk", 3)

print('the maximum length is ', maxl)


















