'''
 Step 1 here: nbb
20 /3 is basically
20 - 3 = 17
17 - 3 = 14
14 - 3 = 11
11 - 3 = 8
 8 - 3 = 5
 5 - 3 = 2

20 /3 = 6       The above is pretty good but you can go even faster,

        20 is the dividend and
        3 is the divisor here

        Quotient is the # of times we can subtract divisor from the dividend here

        quotient = 0 here


1. And then that's only the beginning here,


Situation 2: handling the negatives here

1. Both dividend and divisor are negative, dividend head waay from 0 here.

Some are repeated additions instead of subtractions, and some have <=0

Any negative inputs to positives and then put a


Situation 3: repeated exponential searches

Only subtract 1 copy of the divisor from the dividend, 20 -3
Another solution: subtract multiple at the same time

# say you have a dividend of 93706 and a divisor of 157, we will then see what happens


Must have a lot of data at this point here

This is asa exponential search used for searching sorted spaces kind of like binary search
O(log n)





'''

'''
Remember 20 / 6 
        20 is the dividend and
        3 is the divisor here
            
'''

'''
We will want to fix this situation here, 

Note the reason for this conversion is 

More negative signed 32bit integers than there r positive signed 32-bit integers here 
And also we don't want to treat separate cases for combination of positive/negative div
divisor and dividend as said 

The range of valid negative number is bigger here 


1. Best solution is to work with the negative here 
2. Instead of the positive numbers here 

3

'''


def divide(dividend: int, divisor: int) -> int:
    # Constants.
    MAX_INT = 2147483647  # 2**31 - 1
    MIN_INT = -2147483648  # -2**31
    HALF_MIN_INT = -1073741824  # MIN_INT // 2

    # Special case: overflow.
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    # We need to convert both numbers to negatives.
    # Also, we count the number of negatives signs.
    negatives = 2
    if dividend > 0:
        negatives -= 1
        dividend = -dividend
    if divisor > 0:
        negatives -= 1
        divisor = -divisor

    quotient = 0

    '''
        The case here is basically when the divisor is the bigger element of the 2 here 
    20 the dividend         3 the divisor 
    
    '''
    # Once the divisor is bigger than the current dividend,
    # we can't fit any more copies of the divisor into it anymore */
    while divisor >= dividend:

        # We know it'll fit at least once as divivend >= divisor.
        # Note: We use a negative powerOfTwo as it's possible we might have
        # the case divide(INT_MIN, -1). */
        powerOfTwo = -1

        # value becomes 3
        value = divisor

        '''
        This is the power of the exponential search here, where we can keep doubling the value as said 
        
        '''
        while value >= HALF_MIN_INT and value + value >= dividend:
            value += value
            powerOfTwo += powerOfTwo

        '''
        We have been able to convert things in a different way than the one that you said before here 
        
        
        '''
        # We have been able to subtract divisor another powerOfTwo times.
        quotient += powerOfTwo
        # Remove value so far so that we can continue the process with remainder.
        dividend -= value

    # If there was originally one negative sign, then
    # the quotient remains negative. Otherwise, switch
    # it to positive.
    return -quotient if negatives != 1 else quotient
