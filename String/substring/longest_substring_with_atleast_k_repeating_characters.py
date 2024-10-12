'''
Using this i have


At any point we need to check if numOfUniqChars < curUnique

If numbOfUniqChar < allowedCount:
    expand window from right add a char to the end of window

If numbOfUniqChar > curUnique:
    remove a char frmo the start

For each window check if all char meet the frequency requirement:
    Update the length of each subone
'''
def getMaxUniqueChars(word):
    s = set()
    maxUnique = 0
    for i in range(len(word)):
        char = word[i]
        if char not in s:
            s.add(char)
            maxUnique += 1
    return maxUnique


def longestSubstringUnique(s, k):
    c = dict()
    
    maxUnique = getMaxUniqueChars(s)

    res = 0
    for curUnique in range(1, maxUnique):
        windowStart, windowEnd, idx, countAtLeastK, numUniqueChars = 0, 0, 0, 0, 0

        while windowEnd < len(s):
            # expand the sliding window here
            if numUniqueChars <= curUnique:
                char = s[windowEnd]
                if c[char] == 0:
                    numUniqueChars += 1
                c[char] += 1

                # at least k repeating here
                if c[idx] == k:
                    countAtLeastK += 1
                windowEnd+=1

            # shrink the sliding window here
            else:
                char = s[windowStart]

                # for this letter we have reached k times "aaabc" 3
                if c[char] == k:
                    countAtLeastK-=1
                c[char]-=1

                # if char == a, c[char] == 0, then here it becomes "bc"
                if c[char]== 0:
                    numUniqueChars-=1
                windowStart+=1
            if numUniqueChars == curUnique and numUniqueChars == countAtLeastK:
                res = max(windowEnd- windowStart, res)


    return res

# and then this becomes the code you were saying before

print(longestSubstringUnique("aaabb",3 ))


print(getMaxUniqueChars("aab"))
