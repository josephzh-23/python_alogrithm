package Graph.dfs_with_return

import java.lang.Math.abs
import java.lang.Math.max

// This is the one with the bar graph up here
/*
The approach is DFS + memoization here

 */


/*
 Can jump from index i to j if arr[i] > arr[j]
 and arr[i] > arr[k]
    d is the step to take here
 */


val graph = mutableMapOf<Int, MutableSet<Int>>()

// This store the result of the index and number of times sth
// occurs here
var memo = mutableMapOf<Int, Int>()
fun maxJumps(arr: IntArray, d: Int): Int {
    // An index will have a # of points it can jump to
    // Return # of indices you can visit here
    // And then here
    /*
    Step 1: create a list of points this can jump to
    basically anythign that's smaller
     */
    val n = arr.size
    for (i in 0..n) {

        // to the right here
        for (j in i + 1..n) {

            //break to save time here
            // make sure less than room here
            if (arr[j] < arr[i] && abs(i - j) <= d) {
                graph.computeIfAbsent(i) { mutableSetOf() }.add(j)
            } else break
        }

        // to the left of this
        for (j in i - 1 downTo 0) {
            if (arr[j] < arr[i] && abs(i - j) <= d) {
                graph.computeIfAbsent(i) { mutableSetOf() }.add(j)
            } else break
        }
    }
    var res = 0
    // Step 2 do a dfs here
    for(i in 0..n){
        res = max(res, dfs(i, n))
    }

    return res

}

/*
t: o(nd) (the width we can go in both directions
s: o(nd)

 */

private fun dfs(curIdx: Int, n: Int): Int {
    if(curIdx == n) return 0
    if(graph[curIdx] == null) return 0

    if(memo.contains(curIdx))
        return memo[curIdx]!!

    // If we stay @ current idx, that's considered 1 here
    var path = 1

    for (nextHop in graph[curIdx]!!) {
        // Thisi s jumping to the next one
        path = max(path, 1 + dfs(nextHop, n))
    }
    memo[curIdx] = path
    return path
}