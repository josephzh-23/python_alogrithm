
# Use sorting would be O (n*n)
# using the following would be better
def longestPalindrome(s):

    # Will contain the result here of the palindrome
    res = ""
    resLen = 0

    # for each letter
    for i in range(len(s)):

        # odd length
        l, r = i, i

        # we will start from the middle and scanning outward
        # abbba
        while l >= 0 and r < len(s) and s[l] == s[r]:


            # odd length
            '''
            check the new length of palindrome > the current length of palindrome
            then update the result 
            '''
            if (r - l + 1) > resLen:
                res = s[l:r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

        # even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l: r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return res

str = "josesoj"
res = longestPalindrome(str)
print(res)

