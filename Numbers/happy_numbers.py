
'''

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

You can consistenlty power it by 2 and then do the same for the one above and then 92 nice
this is a good save here and here is the code here

- and then this is what we have at a start and this would be the starting point here
'''


def isHappyNum(n: int) -> bool:
    seen = set()

    while n not in seen:
        seen.add(n)
        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        if total == 1:
            return True
        n = total  # Try again for the summed number
    return False



