a_string = 'Was it a car or a cat I saw'
def palindrome(string):
    string = string.lower().replace(' ', '')
    reversed_string = ''.join(reversed(string))
    return string == reversed_string
print(palindrome(a_string))




#then this is done here as we saw

