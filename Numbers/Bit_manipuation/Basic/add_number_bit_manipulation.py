
'''

Xor (^) gives x and y the sum of x and y

If you take 4 and 5, what does the bit become?

100   4
101   5     Using or

100 (binary)
101 (binary)
001 (binary)    == 1 (decimal)    give you the sum of the 2 bits 





'''
def add(x, y):
    keep = (x & y) << 1
    res = x ^ y


    print("keep and res", keep, res)
    # If bitwise & is 0, then there
    # is not going to be any carry.
    # Hence result of XOR is addition.
    if (keep == 0):
        return res

    return add(keep, res)

add(4, 5)