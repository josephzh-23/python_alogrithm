"""
Given a stinrg, write a fxn to check if it's a permutation of a palindrome
A palindrome: forward and backward same

palindrome = "Tact coa" # Taco Cat
Trick 1 letter would be an odd number (the one in the middle) as mentioned
    and the rest would have even values
"""


#TC: O(n)
def isPalindromPerm(input):
    input = input.replace(" ", "")
    input = input.lower()

# dictionary used to keep track of the count of
# characsters in the string
    d = dict()
    for i in input:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    # used to keep track of whether
    #we have encountered an odd element yet

    # as long as odd_count is 0 it's ok
    odd_count = 0
    for k, v in d.items():

        # not encountered odd yet, this is to find
        # the middle letter (the one with odd count)
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1

        # an odd count has already happened
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"
print(isPalindromPerm(palin_perm))
print(isPalindromPerm(not_palin_perm))
