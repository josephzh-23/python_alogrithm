package String.Hard

import java.lang.Math.abs

// https://leetcode.com/problems/first-missing-positive/description/
// One of the hardest probably ever
/*
We could be doing this using a set but probably not so good
since it has O(n) SC
 */


// Say if you have 1, 2, 4      the first missing is then 3
fun firstMissingPositiveInteger(nums: IntArray): Int { // This has to be done in O(1) time as explained before

    if (nums == null || nums.size == 0) return 1
    var n = nums.size
    var containsOne = 0


    /*
    Step 1:
    We know the number is within the range n, first everything (abs(nums[i]) > n or negative
    we make them 1
    so [7, -2, 3, 1, 2, 20, -5]
    make it   [7, 1, 3, 1, 2, 1, 1]
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


    /*
    Step 2:
    make o(1) remove the need for set the tricky part, convert the element to the index
    and swap the sign
     [7, 1, 3, 1, 2, 1, 1]
    [-7, -1, -3, 1, 2, 1, -1 ]
    */
    // Make it negative first
    for(i in 0 until n){
        var index = abs(nums[i]) - 1        // -1 because it's index based and we have 1 based

        // By making it -1 means we have seen the value
        if(nums[index] > 0) nums[index] = -1 * nums[index]
    }

    // step 3 find the first value that's greater than 1?
    // [-7, -1, -3, 1, 2, 1, -1 ]
    // at 1, the index is 3 so we do 3 + 1 = 4 that's our missing number here
    for(i in 0 until n){
        if(nums[i] > 0){
            return i + 1
        }
    }
    // [1, 2, 3] -> 4
    return n + 1
}