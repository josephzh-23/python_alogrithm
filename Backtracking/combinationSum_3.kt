package Backtracking

import java.util.*


//Backtracking.combinationSum here

// https://leetcode.com/problems/combination-sum-iii/

/*
The problem is as shown above and you can see that
 */



fun combinationSum3(k: Int, n: Int): List<List<Int?>?> {
    val result: MutableList<List<Int>> = ArrayList()
    combinations(1, k, n, LinkedList<Int>(), result)
    return result
}

// What's k here? the number of here
private fun combinations(start: Int, k: Int, n: Int, temp: LinkedList<Int>, result: MutableList<List<Int>>) {
    if (k < 0 || n < 0) return
    if (k == 0 && n == 0) {
        result.add(ArrayList(temp))
        return
    }
    for (i in start..9) {
        temp.add(i)

        // 1, 2, 3, 4,
        // n- i     = the remaning result
        combinations(i + 1, k - 1, n - i, temp, result)
        temp.removeLast() // backtrack
    }
}


fun main() {

    var intarr = intArrayOf(2, 3, 6, 7)
  combinationSum3(3, 7)
}