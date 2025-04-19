
'''
ab | ba

left and then right here

ab |c| ba

If it is odd, expand left = (i-1) and right = (i+1)
If it is even, expand left = (i) and right = (i+1)

O(n^2)
Here done without using the crazy solution
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