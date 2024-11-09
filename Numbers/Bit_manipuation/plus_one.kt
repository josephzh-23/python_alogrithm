package Numbers.Bit_manipuation
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.


Input: digits = [1,2,3]
Output: [1,2,4]





fun main() {
    //
    var arr = intArrayOf(1, 2, 3)
    plusOne(arr)
}
fun plusOne(digits: IntArray): IntArray {
    var digits = digits
    val n = digits.size

    // So this will only be n- 1 all the way down to 0 here
    for (idx in n - 1 downTo 0) { // set all the nines at the end of array to zeros
        if (digits[idx] == 9) {
            digits[idx] = 0
        } else { // increase this rightmost not-nine by 1

            println("here the digit is ${digits[idx]}")
            digits[idx]++ // and the job is done
            return digits
        }
    }

    // we're here because all the digits are nines
    digits = IntArray(n + 1)
    digits[0] = 1
    return digits
}