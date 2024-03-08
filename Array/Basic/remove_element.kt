package Array.Basic

/*

This is the basic questino here very important
 */

fun main() {
    var nums = intArrayOf(3, 2, 2, 3)
    var value = 3
    removeElement(nums, value)
}

/*
This has to be done in place as said
Using the 2 pointer solutino here
 */
fun removeElement(nums: IntArray, value: Int): Int {
    var i = 0

    for (j in 0 until nums.size) {

        // 2, 2, 3, 3
        // 2, 2, _ , _
        if (nums[j] != value) {
            nums[i] = nums[j]
            i++


        // 2, 2, _ , _ in teh above case nothign happens
        } else { // nothing happens here
        }
    }
    return i
}