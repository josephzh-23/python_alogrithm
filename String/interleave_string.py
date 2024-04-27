'''

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

s1 = aabcc      s2 = dbbca      # here and then the code becomes
s3 = aadbbcbcaca            # true here

Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".

And then we ahve the code below here:


Here we will deal with this
'''
# Brute force approach here
# o(2 ^ m +n)s
def is_InterLeave(s1, i, s2, j, res, s3):

    '''
    I and j used to iterate throgh the s1 and s2 as said here
    '''
    if res == s3 and i == len(s1) and j == len(s2):
        return True

    ans = False


    ''' 
    And then using this this then becomes 
    
s1 = aabcc      s2 = dbbca      # here and then the code becomes
s3 = aadbbcbcaca    

    So we go thru aa (s1) -> dbb (s2) -> bcc(s1) -> s2
    
    '''
    if i < len(s1):
        ans |= is_InterLeave(s1, i + 1, s2, j, res + s1[i], s3)
    if j < len(s2):
        ans |= is_InterLeave(s1, i, s2, j + 1, res + s2[j], s3)
    return ans

# this is the entry point here
def isInterLeave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    return is_InterLeave(s1, 0, s2, 0, "", s3)


print(isInterLeave("aabcc", "dbbca", "aadbbcbcac"))