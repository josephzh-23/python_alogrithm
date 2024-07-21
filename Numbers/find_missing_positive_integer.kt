package String.Hard

import java.lang.Math.abs

// One of the hardest probably ever
/*
We could be doing this using a set but probably not so good
since it has O(n) SC
 */
fun findMissingPositiveInteger(nums: IntArray): Int { // This has to be done in O(1) time as explained before

    if (nums == null || nums.size == 0) return 1
    var n = nums.size
    var containsOne = 0


    // The size is the most important thing here remember

    /*
    [7, 1, 3, 1, 2, 1, -1]
    [-7, -1, -3, 1, 2, 1, -1]       after transform here

    And fidn the first positive integer here 1 which is at index 3  (3 + 1) = 4
    that's
     */

    // step 1
    for (i in 0 until n) {
        if (nums[i] == 1) {
            containsOne = 1
        }else if (nums[i] <= 0 || nums[i] > n){
            nums[i] =1
        }
    }

    if(containsOne == 0) return 1
    // Make it negative first
    for(i in 0 until n){
        var index = abs(nums[i]) - 1

        if(nums[index] > 0) nums[index] = -1 * nums[index]
    }

    // step 3 find the first value that's greater than 1?
    for(i in 0 until n){
        if(nums[i] > 0){
            return i + 1
        }
    }
    // [1, 2, 3] -> 4
    return n + 1
}