'''

Always in the form "XYX" here,
Find 1st and last occur of x in the string here

2.

'''
from palindrome.is_subsequence import isSubsequence


def uniqueLength3PalindromicSubsequence(word):
    c = 'a'
    l, r = 0, len(word) -1
    for a in word:
        if word[l] == word[r]:

            for i in range(l + 1, r):
                # switch each letter 'aaa' -> 'ababa'

                # while ord(c) <= ord('z'):
                #     checkedWord = word[l] +chr(ord(c)) + word[r]
                #     c = chr(ord(c) + 1)
                #     print(checkedWord)


uniqueLength3PalindromicSubsequence("aabca")