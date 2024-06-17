package String.Basic

/*

Given a non-empty array of integers nums,
 every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [2,2,1]
Output: 1



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