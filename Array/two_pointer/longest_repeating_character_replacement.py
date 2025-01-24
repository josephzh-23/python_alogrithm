
'''
AABABBA
 ^
     ^
k = 2
{A: 2, B: 3}            numOfCharacterReplacement = (right- left + 1) - mostFreq
maxLen = 5              condition: (right - left + 1) - mostFreq > k
mostFreq =3
'''

# k = # of times u can replace sth
def characterReplacement(s, k):
    l, r = 0, 0
    n = len(s)
    # use a hash map to keep track
    dict = {}
    maxlen = 0
    mostFreq = 0

    # find longest repeating char replacement
    while (r < n):
        #Expand the sliding window

        '''
        Need to create the above dictionary values 
        {A: 2, B: 3}
        '''
        dict[s[r]] = dict.get(s[r], 0) + 1

        # compare the mostFreq with the current char frequency
        mostFreq = max(mostFreq, dict.get(s[r]))

        # condition: (right - left + 1) - mostFreq > k
        '''
        shrink the window if we need to replace more than k char
        this means increase the left pointer
        
        also need to change {A: 3, B: 3} 
        to {A: 2, B: 3}     since we are moving the left pter forward 
        '''
        if (r- l +1) -mostFreq > k:

            dict[s[l]] = dict.get(s[l] - 1)
            l +=1
        maxlen = max(maxlen, r- l + 1)


        r+=1
    return maxlen

s = "ABABA"
s2 = "HHHHHH"
print("Maximum length =",
             characterReplacement(s, 2))