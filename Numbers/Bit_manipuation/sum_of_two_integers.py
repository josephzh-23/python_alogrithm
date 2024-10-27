'''
Step 1:Using xor

adding 2 bits with no carry
Xor for addition

1 xor 1 is 0      (same as 1 + 1 == 0 but no carry)
1 xor 0 is 0      (same as 1 + 0 == 1)

Step 2: Using and for carry

1) The and operation gives a binary number that represnts the bits with a carry


Step 3: Shfit for the carry

left shift the carry to 1, so it would go to the next bit higher here,

Step 4: Iteration until no more carry

 We need to repeat this process until there is no carry left, i.e., the result of the AND operation is 0.


 Step 5: How to take care of the negative case here?

 Masking with 0xFFFFFFFF: To ensure compatibility with negative numbers and
 to simulate 32-bit integer overflow behavior, bitwise operations are performed with a mask of 0xFFFFFFFF.

 Step 6: Check for negative result

 If the result has its leftmost bit (bit 31) set, it is negative (in 32-bit two's complement form).
 To convert it to a negative number that Python recognizes, the inverse operation is applied (via ~(a ^ 0xFFFFFFFF)).
'''


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to get 32-bit representation
        MASK = 0xFFFFFFFF

        # Convert a and b to 32-bit integers
        a, b = a & MASK, b & MASK

        # Iterate while there is a carry
        while b:

            # Calculate the carry from a and b,
            # and ensure it's within the 32-bit boundary
            carry = ((a & b) << 1) & MASK

            # XOR a and b to find the sum without considering carries,
            # then consider the carry for the next iteration
            a, b = a ^ b, carry

        # If a is within the 32-bit integer range, return it directly
        # The operation 'a < 0x80000000' checks if the result is within the positive range
        # of a 32-bit integer (from 0x00000000 to 0x7FFFFFFF)
        if a < 0x80000000:
            return a

        # If a is outside the 32-bit integer range, which means it is negative,
        # return the two's complement negative value, which is the bitwise negation of a
        # (by XORing with MASK, which is 'all 1's for a 32-bit number') and adding 1
        return ~(a ^ MASK)
