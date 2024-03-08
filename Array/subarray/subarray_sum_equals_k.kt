package Array.subarray


fun main() {
    var nums = intArrayOf(1, 1, 1)
    var k = 2
    println(subarraySum(nums, 2))
}

// Subarray equals sums k in leetcode
/*

Given an array of integers nums and an integer k,
 return the total number of subarrays whose sum equals to k.
 Input: nums = [1,2,3], k = 3
Output: 2
 */
// Need to work on the prefix sum problem here
fun subarraySum(nums: IntArray, k: Int): Int {

    /*
    3   4   7    2          k = 7
 0  3   7   14   16         we have to add the sum here

 @ each iteration then we have 7 -7 = 0, so that means we found 1, then we add that to the
 code or our dict here
     */
    // See the notes
    var dict = mutableMapOf<Int, Int>()

    // This is the part of the trick here too
    dict[0] = 1
    var n = nums.size
    var count = 0
    var s = 0

    for (num in nums) {
        s += num
        // The case where 14 - 7 is already in there
        if (dict.contains(s - k)) {
            dict[s - k]?.let {
                count += it
            }
        }

        // The case 2 where if already seen the sum 14
        if (dict.contains(s)) {
            dict[s] = dict[s]!! + 1
        }
        // The case if havent seen before here
        else {
            dict[s] = 1
        }

    }
    return count
}
