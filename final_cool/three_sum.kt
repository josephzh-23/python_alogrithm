package final_cool

import java.util.*


// watch out for the duplicate here

/*
The process is very simple
You keep below
[ -3  -3   -1   2   3   4]
  a   L                 R

You keep it at -3 and do a 2 sum for L and R can then get an O(n^2) as said

 */

fun threeSum(nums: IntArray): List<List<Int>> {
    val list: MutableList<List<Int>> = ArrayList()
    Arrays.sort(nums)
    val n = nums.size
    for (i in 0 until n - 2) {
        if (i == 0 || i > 0 && nums[i] != nums[i - 1]) {
            var l = i + 1
            var r = n - 1
            while (l < r) {
                if (nums[l] + nums[r] == -1 * nums[i]) {
                    list.add(Arrays.asList(nums[i], nums[l], nums[r]))

                    // Avoid left and right duplicate here so nothing like that going on
                    // here
                    while (l < r && nums[l] == nums[l + 1]) l++
                    while (l < r && nums[r] == nums[r - 1]) r--
                    l++
                    r--
                } else if (nums[l] + nums[r] < -1 * nums[i]) l++ else r--
            }
        }
    }
    return list
}