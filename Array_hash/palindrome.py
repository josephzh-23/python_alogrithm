# backward and forwad would give the same value


'''
A palindrome is a word that reads the same
forward and also backward

kayak
madam
'''

def palindrome(string):
    string = string.lower().replace(' ', '')

    reversed_string = ''.join(reversed(string))
    return string == reversed_string
print(palindrome(a_string))


# Approach 2: using 2 poitner approach


#then this is done here as we saw

