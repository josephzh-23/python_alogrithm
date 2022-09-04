

'''
The input array would be sorted here
Input: numbers = [1, 3, 4, 5, 7, 11], target = 9
                  l
                     r
                     1 + 3 = 4 no -> so mv r forward
                     yes -> add to the list then

                     that's the difference between the 2 then.
Output: [4, 5]
'''

# ABBA


# using 2 pters
'''
ABCD
DCBA
'''
def reverseString(s):
    l, r = 0, len(s)-1

    for i in range(len(s)):
        #swap
        temp = s[l]
        s[l]= s[r]
        s[r] = temp

    return s
print(reverseString("JOseph"))