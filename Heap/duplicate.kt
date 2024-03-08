//package Heap
//
//import java.util.*
//
//class Interval internal constructor(var start: Int, var end: Int)
//internal class Solution {
//    fun search(intervals: Array<Interval>, nums: IntArray, target: Int): Int {
//        Arrays.sort<Interval>(intervals) { a, b -> a.start - b.start }
//        var start = 0
//        var end = nums.size - 1
//        while (start < end) {
//            val mid = start + (end - start) / 2
//            if (nums[mid] == target) {
//                return mid
//            } else if (nums[mid] > target) {
//                end = mid
//            } else {
//                start = mid + 1
//            }
//        }
//        return if (nums[start] == target) {
//            start
//        } else -1
//    }
//}