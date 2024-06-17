'''


Input: s = "011101"
Output: 5
Explanation:
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5
left = "01" and right = "1101", score = 1 + 3 = 4
left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2
left = "01110" and right = "1", score = 2 + 1 = 3

The score after splitting a string is the number of zeros
in the left substring plus the number of ones in the right substring.

This is an easy problem here
'''
def maxScore(s: str)-> int:
    zero = 0
    one = s.count('1')
    res = 0

    for i in range(len(s) -1):
        if s[i] == '0':
            zero+=1
        else:
            one-=1
        res = max(res, zero + one)
    return res