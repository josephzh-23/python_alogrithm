package Dynamic_programming.`2d_programming`

import java.util.*


/*
Problem taken from Coding Ninjas up there
1. You are given an array of n positive integers and integer k, check if there
exists a subset in ARR with a sum = to k
2. Return true if there exists a subset with sum = k. otherwise return false

If arr = [1, 2, 3, 4]    k = 4
there exists 2 subset with sum [1, 3] and [4]

 */

/*
TC: O( n* target)
SC: O (n *target) + O(n)
At every turn, we either include or not include elem in sequence

1. Exclude cur elem,    f(ind -1, target)
2. Include cur elem     f(ind -1, target - arr[ind])
        since we are considering so minus from the total
 */



internal object TUF7 {
    fun subsetSumUtil(idx: Int, target: Int, arr: IntArray, dp: Array<IntArray>): Boolean {

    // The base case and then
     /*
     If target == 0, it means that we have already found the subsequence from the
previous steps, so we can return true.
      */
        if (target == 0) return true

        /*
        If ind==0, it means we are at the first element,
 so we need to return if arr[ind]==target,
 If the element is equal to the target we return true else false.
         */
        if (idx == 0) return arr[0] == target

        // -1 is the unvisited state, so if we already have 1 (from the stored state)
        // We can return the below
        if (dp[idx][target] != -1) return if (dp[idx][target] == 0) false else true

        // If choose not to exclude, target the same,
        val notTaken = subsetSumUtil(idx - 1, target, arr, dp)

        // False at beginning,when do we take the target
        /*
            if (target >= a[idx]    Ex: [1, 3, 6]   tar =2
            then you can't take a[idx]  (can't take 3, 6)
         */
        var taken = false

        // If 3 < 4, then we can include and below is decision for include
        if (arr[idx] <= target) taken = subsetSumUtil(idx - 1, target - arr[idx], arr, dp)
        dp[idx][target] = if (notTaken || taken) 1 else 0
        return notTaken || taken
    }

    fun subsetSumToK(n: Int, k: Int, arr: IntArray): Boolean {

        /*
        Main pts
        1. Create a dp array of size [n][k+1], a 2d array, size of input is 1
        initially everything in the row will be filled with -1 as said
         */
        val dp = Array(n) { IntArray(k + 1) }
        //init all array with -1
        for (row in dp) Arrays.fill(row, -1)


        /*
         dp[idx][tar] will have 3 states: 0, 1, -1
         -1 will be at beginning, before include or exclude
         0 is when not include, 1 is when you include sth here
         */

        // This is using bottom up approach (from back)
        return subsetSumUtil(n - 1, k, arr, dp)
    }

    @JvmStatic
    fun main(args: Array<String>) {
        val arr = intArrayOf(1, 2, 3, 4)
        val k = 4
        val n = arr.size
        // Starting from the back, k is the target
        if (subsetSumToK(n, k, arr)) println("Subset with given target found") else println("Subset with given target not found")
    }
}