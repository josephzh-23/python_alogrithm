//package Backtracking
//
//import java.util.*
//
//
//// Using the subset 2 problem here
//
///* This Question is exactly similar to Subsets - I.
//Instead of All Unique Elements we have given an array nums[] containing Dupicate Elements
//Our Logic remains the same. We will generate Subsets by using - Pick & Don't Pick condition only
//Only difference is that, while we are not picking any element, we must skip all it's Duplicate occrurrences in nums[] .
//This can be acheived by using a While Loop. Also we need to sort nums[] as the array might be given as unsorted
//*/
//internal class Solution {
//    fun subsetsWithDup(nums: IntArray): List<List<Int>> {
//
//        // In this logic we to sort the array
//        Arrays.sort(nums)
//        val ans: MutableList<List<Int>> = ArrayList()
//        helper(nums, 0, ArrayList(), ans)
//        return ans
//    }
//
//    fun helper(nums: IntArray, i: Int, subset: MutableList<Int>, ans: MutableList<List<Int>>) {
//        // Our base case will hit when our i pointer reaches the end of given array nums[]
//        var i = i
//        if (i == nums.size) {
//            ans.add(ArrayList(subset))
//            return
//        }
//
//        // We pick i-th Element
//        subset.add(nums[i])
//
//        // We ask recursion to do rest of the task
//        helper(nums, i + 1, subset, ans)
//
//        // Backtrack and Undo the change we have done
//        subset.removeAt(subset.size - 1)
//
//        // While using Don't Pick option, we must ensure we skip all the Duplicate Occurrences of nums[i]
//
//        while (i < nums.size - 1 && nums[i] == nums[i + 1]) {
//            i++
//        }
//
//        // Our i pointer will stop on the last Duplciate Occurencce of nums[i]
//
//        // Don't Consider the Element and Ask Recursion to generate Unique Subsets
//        helper(nums, i + 1, subset, ans)
//        return
//    }
//}
//
///*
//Time Complexity : O(2^N)
//Space Complexity : O(N)
//*/