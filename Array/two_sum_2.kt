package Array

import January_3rd.print

// https://leetcode.com/problems/two-sum/description/
// Here since the input is sorted

// Using 2 sum in leetcode over here and then what's the solutino
// 2 sum 2
/*

 Say if the num is [1, 3, 4, 5, 7, 11]
 And the target is 9        1 + 11 = 12 > 9
                            1 + 7  = 8 < 9 and then move the 2 pointers here

 So we will add the sum to check
 */

fun main() {
    var nums = intArrayOf(1, 3, 4, 5, 7, 11)
    sol(nums, 9).print()
}
fun sol(num: IntArray, target:Int) : Pair<Int, Int>{
    // Can use a 2 input solutinos
    var l = 0
    var r = num.size - 1
    for(i in 0 until num.size){
        var sum = num[l] + num[r]
        if(sum == target){
            return Pair(l, r)
        }else if(sum > target){
            r--
        }else if(sum < target){
            l++
        }
    }
    return Pair(l, r)
}
