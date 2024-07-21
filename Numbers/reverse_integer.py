'''
This is the code here

'''

def reverseInteger(x):
    rev = 0

    sign = [1, -1] [ x < 0]
    x = abs(x)

    while x:

        # pop the last digit that came off
        lastDigit = x %10
        x /= 10

        rev = rev * 10 + lastDigit

        if rev > 2 ** 31 -1:
            return 0
    return sign * rev