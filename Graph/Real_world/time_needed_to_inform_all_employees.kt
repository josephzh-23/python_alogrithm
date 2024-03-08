package Graph.Real_world

import java.util.*
import kotlin.math.max


/*

If the n is 6 and head id = 2,
    manager = [2, 2, -1, 2, 2, 2]
inform time = [0, 0, 1, 0, 0,0 ]
 */

/*
 Using a bfs with adj list here pretty much, the manager will have manager array here

 */
fun numOfMinutes(n: Int, headId: Int, manager: IntArray, informTime: IntArray): Int {


    var adj = mutableMapOf<Int, MutableList<Int>>()
    for (i in 0 until n) {
        var managerIndex = manager[i]

        adj.computeIfAbsent(managerIndex) { mutableListOf<Int>() }.add(i)
    }

    var q = LinkedList<IntArray>()
    q.add(intArrayOf(headId, 0))
    var res = 0
    while (q.isNotEmpty()) {
        var (i, time) = q.pop()
        res = max(res, time)

        adj[i]?.run {
            for (emp in this) {
                q.add(intArrayOf(emp, time + informTime[i]))
            }
        }
    }
    return res
}

fun main() {
    var n = 6;
    var headId = 2
    var manager = intArrayOf(2, 2, -1, 2, 2, 2)
    var informTime = intArrayOf(0, 0, 1, 0, 0, 0)
    print(numOfMinutes(6, headId, manager, informTime))
}