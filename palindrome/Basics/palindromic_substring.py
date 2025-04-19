'''



Get number of substrings in a palindrome words
Expand around the center here

-

This solutino below does not make use of the Manacher's algorithm
The solution uses an algorithm known as "Manacher's Algorithm", which is efficient for finding palindromic substrings. The key idea is to avoid redundant computations by storing and reusing information about previously identified palindromes.
=
'''


def countSubstrings(self, s: str) -> int:
    n, ans = len(s), 0

    def palindromeCount(left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1
        return count

    for i in range(n):
        even = palindromeCount(i, i + 1)
        odd = palindromeCount(i, i)
        ans += even + odd

    return ans