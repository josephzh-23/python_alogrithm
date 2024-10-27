'''
Given an integer num, repeatedly add all its digit
s until the result has only one digit, and return it.

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.


Check the base number here let's try doing this using recursion here

Check the base case here
- Check the given num we have to iterate the number again and again until it gets the single digit number

- After getting the Number if it is Single Digit the return it, otherwise the calculated number goes in the recursive call.
'''
# and this is the sort of solution that we are currently looking for here
# using this formula here # and this is pretty good as said here
class Solution:
    def addDigits(self, num):
        digit_sum = 0

        if num < 10:
            return num

        while num:
            digit_sum += num % 10
            num = num // 10

        return self.addDigits(digit_sum)
