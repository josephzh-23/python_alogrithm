'''
Then when we use
(a & b) << 1
because you have the carry here carry = ( x & y ) << 1 as above mentioned

Why do we have the carry digit here?
Basically you have the code here

         1 0 0 1     a
         1 0 1 1     b

a^b      0 0 1 0
a&b<<1 1 0 0 1 0

 And then use xor on the above 2 numbers here

 ^    1 0 0 0 0
&<<1  0 0 1 0 0  

'''