package Graph

/*

What we can do
1. Every time see gate run a Graph.Edges_question.dfs from it and then this
2. This will reach all the cells in the range
3. Pass a count in the Graph.Edges_question.dfs 1 and make sure it has the shortest distance
 */



import java.util.*


var res = 214

var matrix2 = arrayOf(
        intArrayOf(214, -1, 0, 214),
        intArrayOf(214, 214, 214, -1),
        intArrayOf(214, -1, 214, -1),
        intArrayOf(0, -1, 214, 214)
);

/*
We will start the distance from the gate first
1. So when we see a gate we will start this
 */


private val dirs = arrayOf(intArrayOf(0, -1), intArrayOf(0, 1), intArrayOf(-1, 0), intArrayOf(1, 0))
fun wallsAndGates(rooms: Array<IntArray>) {
    if (rooms.size == 0 || rooms[0].size == 0) return
    val m = rooms.size
    val n = rooms[0].size
    val visited = Array(m) { BooleanArray(n) }
    val pq: Queue<IntArray> = LinkedList()
    for (i in 0 until m) {
        for (j in 0 until n) {
            if (rooms[i][j] == 0) {
                pq.add(intArrayOf(i, j))
            }
        }
    }
    var cur = 0
    while (!pq.isEmpty()) {
        cur++
        val sz = pq.size
        for (ii in 0 until sz) {
            val np = pq.poll()
            for (dir in dirs) {
                val x = np[0] + dir[0]
                val y = np[1] + dir[1]
                if (x >= 0 && x < m && y >= 0 && y < n && rooms[x][y] != 0 && rooms[x][y] != -1 && !visited[x][y]) {
                    visited[x][y] = true
                    // Modifiy this over here xs
                    rooms[x][y] = cur
                    pq.add(intArrayOf(x, y))
                }
            }
        }
    }
    println(rooms)
}

fun main() {
    wallsAndGates(matrix2)

}

// This makes sure no array out of bound exception here






