'''
This should be done using java b/c we have the overflow case in the

Additive operation
Using bitwise XOR and ANR operations to perform additive operation,

a XOR b (a ^ b): form bitwise     sum of a+b w/o carry
a AND b (a & b): form bitwise     carry of a+b

But after the carry is calculated, we shift it left by 1 here
So really the result is
a + b = a XOR b + ((a AND b) << 1)
      = a ^ b + ((a & b) << 1)
'''

public int getSum(int a, int b){
    while(b!= 0){

    // the carry here
        int tmp = (a &b) <<1
        a = a ^b
        b = tmp


    }
    return a

}