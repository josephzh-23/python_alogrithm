package Backtracking

import January_3rd.print


// Basically at each decision we either include or we don't include

class s{
    // Note that having the above here will not work
    // this will not get the value, must have it inside the function
//    var res = mutableListOf<MutableList<Int>>()
    var target = 0

    fun dfsStart(cand: IntArray, tar: Int){
        target = tar
        val res = mutableListOf<MutableList<Int>>()
        dfs(cand, 0, mutableListOf(), 0, res)
        println(res)
    }

    fun dfs(cand: IntArray, i: Int, cur: MutableList<Int>, total: Int,
    res: MutableList<MutableList<Int>>) {
        if (total == target) {
            // Here it's important to add the copy
            res.add(ArrayList(cur))
            return
        }
        if (i >= cand.size || total > target) {
            return
        }
        cur.add(cand[i])

        // WHen we include the cur element
        dfs(cand, i, cur, total + cand[i], res)
        // We skip the current element, so total stays the same
        cur.removeLast()
        dfs(cand, i + 1, cur, total, res)
    }
}

fun main() {
    var s = s()
    s.dfsStart(intArrayOf(2, 3, 6, 7), 7)
}