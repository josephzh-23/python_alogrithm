
package Backtracking

//https://leetcode.com/problems/combination-sum/
fun combinationSum(candidates: IntArray, target: Int): List<List<Int?>?> {
    val result: MutableList<List<Int>> = ArrayList()
    backtrack(candidates, 0, target, ArrayList<Int>(), result)
    return result
}

private fun backtrack(cand: IntArray, start: Int, target: Int, list: MutableList<Int>, result: MutableList<List<Int>>) {
    if (target < 0) return
    if (target == 0) result.add(ArrayList<Int>(list))
    for (i in start until cand.size) {
        list.add(cand[i])
        backtrack(cand, i, target - cand[i], list, result)
        list.removeAt(list.size - 1)
    }
}