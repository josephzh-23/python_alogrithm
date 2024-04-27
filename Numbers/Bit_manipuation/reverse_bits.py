
'''
step 1:
We iterate through the bit string of the input integer, from right to left (i.e. n = n >> 1).
 To retrieve the right-most bit of an integer, we apply the bit AND operation (n & 1).
1 0 1 1
      1     (all the areas before 1 considered 0) here
0 0 0 1

step 2:
For each bit, we then reverse it to teh right position using the following:
(n & 1) << power , then add it to the final result here

'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

