'''

Part 1:
a ^ b is part 1 of adding 2 numers without carry

Part 2:
Then when we use
(a & b) << 1
because you have the carry here carry = ( x & y ) << 1 as above mentioned



part 1:
a       1 0 0 1
b       1 0 1 1

a^b     0 0 1 0
carry 1 0 0 1 0         (a & b) << 1


part 2: take above 2 numbers and add them toegther
Do another xor and carry
^       1  0  0  0  0
&<<1    0  0  1  0  0


 And then use xor on the above 2 numbers here

 ^    1 0 0 0 0
&<<1  0 0 1 0 0  
      1 0 1 0 0 
'''