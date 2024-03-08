package Numbers.Bit_manipuation

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