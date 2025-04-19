from typing import List
'''

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

The input above looks like that s
'''

def shiftingLetters(s: str, shifts: List[int]) -> str:
    n, t = len(s), 0
    s = list(s)
    for i in range(n - 1, -1, -1):
        t += shifts[i]
        s[i]= chr((ord(s[i]) - ord('a') + t) % 26 + ord('a'))
    return ''.join(s)

print(shiftingLetters('abc', [3, 5, 9]))