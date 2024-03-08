package Recursion

//https://leetcode.com/problems/partition-equal-subset-sum/
/*
Approach
1. Divide sum /2
2. And then decide take/skip minusing the value to see what's left

Thi s is the bad approach because of duplicate as mentinoed before
 */
// This is an important function here for skipping or returning values
fun main() {
    // Check if you can find sum in the given array
    var arr = intArrayOf(1, 2, 3, 100)

    var sum = arr.sum() / 2
    takeOrSkip(sum, arr, 0).also { print(it) }
}

fun takeOrSkip(sum: Int, arr: IntArray, index: Int): Boolean {
    if (index >= arr.size || sum < 0) return false
    if (sum == 0) return true

    // Using take or skip below we can know whether there is any subset
    // inside the array sum up to the sum here
    val take = takeOrSkip(sum - arr[index], arr, index + 1)
    val skip = takeOrSkip(sum, arr, index + 1)
    return take || skip
}