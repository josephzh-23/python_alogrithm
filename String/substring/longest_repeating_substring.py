'''

helper(mid) = 4 here

How to implement this helper function here
The length of the repeating string here

Check if we have seen this before

If we have abcdef

wanna stop at d
'''

def longestRepeatingSubstring(s):
    n = len(s)

    left , right = 0, n- 1

    while left < right:
        mid = left + (right - left + 1)//2

        if findRepeatingSubString(mid, n, s):
            left = mid
        else:
            right = mid -1
    return left
def findRepeatingSubString(n, length, s):
    seen = set()
    # we want to stop at d in -> abcdef
    for i in range(n- length + 1):
        substring = s[i :i + length]


        if substring in seen:
            return True
        seen.add(substring)

    return False





