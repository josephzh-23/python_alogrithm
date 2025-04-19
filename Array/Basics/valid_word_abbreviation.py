
'''

The trick here using a 3rd variable to do this here
Input: word = "internationalization", abbr = "i12iz4n"
Output: true
And that's the one above here and that's actually quite interesting here


Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

'''



def validWordAbbreviation( word, abbr):
    i = j = 0
    m, n = len(word), len(abbr)
    while i < m and j < n:

        print('i and j are', i, j )
        if word[i] == abbr[j]:
            i += 1
            j += 1
        elif abbr[j] == "0":
            return False

            '''
            Input: word = "internationalization", abbr = "i12iz4n"
            
            What's this saying is 
            j = 1
            abrr[j] = 1 
            k = 1
            
            k = 2
            abrr[2] =  2
            
            i = 13 (b/c previously is 1)
            j = 3                
            '''
        elif abbr[j].isnumeric():
            k = j
            while k < n and abbr[k].isnumeric():
                k += 1
            i += int(abbr[j:k])
            j = k
        else:
            return False
    return i == m and j == n

validWordAbbreviation(word  = "internationalization", abbr = "i12iz4n")
