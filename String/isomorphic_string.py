'''

And then let's work on this again here



e -> a


Use the word paper and title

a= ord['p']
b = ord['t']


d1[a] and d1[b]

- and then here we have the code

Both are 0 first

1. d1[a] and d2[b]

Both are 0 not seen before here,

- d1[a] = 1 and d2[b] = 1


2. And then

a = ord('a') and b = ord('i')


Each character's ASCII is a valid index here and then using this we have

1.
'''


def isIsomorphic( s: str, t: str) -> bool:
    # Create two arrays to store the last seen positions of characters
    # from strings 's' and 't'.
    mappingDictSToT = [-1] * 256
    mappingDictTToS = [-1] * 256

    # and the above makes sense here

    for i in range(len(s)):

        # the 2 characters above here and then
        c1 = s[i]
        c2= t[i]


        # case 1 no mapping exists here and then

        if mappingDictSToT[c1] == -1 and mappingDictTToS[c2] == -1:
            mappingDictSToT[c1] = c2
            mappingDictTToS[c1] = c1


        elif not mappingDictTToS[c1] == c2 and mappingDictSToT[c2] == c1:
            return False

        # and then here is where it's false here


    # and then the code here is quite interesting indeed and then that's the first equation that we can think of here
    return True
'''
The positions as seen here are 

lastSeen1[p]: 2
lastSeen2[t]: 

'''
print(isIsomorphic("paper", "title"))
