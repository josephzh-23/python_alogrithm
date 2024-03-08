package Numbers.Bit_manipuation

/*
The idea is to use XOR opeartor here
And then using the result here

Find the number that's different
 */

fun main() {
    var arr = intArrayOf(4, 1, 2, 1,2)
    print(singleNumbers(arr))
}
fun singleNumbers(numbers: IntArray): Int {
    var result = 0 // The desired signle number here
    for (num in numbers) {
        result = result xor num
    }
    return result
}