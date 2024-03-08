package Trial

import January_3rd.print

/*
xor = 1 if 2 bits are different
= 0 if 2 bits are the same
Remember here 0 xor x = x
xor of 2 equal bits become 0 xor 0 = 0

Xor : if you want to sum 2 bits with no carry here

Finding the carry:
and of 2 input numbers shifted 1 bit to the left carry = ( x& y) << 1

And operator:  (a && b) << 1
number = 1 if both bits are 1 here
So this will be shifted to the left by 1 here
 */

fun main() {
    getSum(1, 3).print()
}
fun getSum(a: Int, b: Int): Int {
    var a = a ; var b = b
    while(b!= 0){
        // For the carry and
        var tmp = (a and b) shl 1
        a = a xor b
        b = tmp
    }

    return a
}















