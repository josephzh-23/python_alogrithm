'''


Here the question return sum without using the additive oepration here


Additive operation
Using bitwise XOR and ANR operations to perform additive operation,

a XOR b (a ^ b): form bitwise     sum of a+b w/o carry
a AND b (a & b): form bitwise     carry of a+b

But after the carry is calculated, we shift it left by 1 here
So really the result is
a + b = a XOR b + ((a AND b) << 1)
      = a ^ b + ((a & b) << 1)
'''


''' case 2 
Overflowing case here, and then we have 
while (mask & b) > 0 here that's first 

If < 0      this is where overflowing happens 

return ( mask & a ) if b> 0 
this takes first 32 bits of the value here 
'''

def getSum(a: int, b: int)-> int:

    # python
    mask = 0xfffffff

    # if < 0 then overflow will happen here
    while (mask&b) > 0:
        a, b = a^b, (a&b) <<1

    return (mask&a) if b> 0 else a