package Graph


fun main() {
    var edges = arrayOf(intArrayOf(0, 1),
            intArrayOf(0, 2), intArrayOf(2, 3), intArrayOf(3, 4), intArrayOf(5, 6))
    countComponentsdfs2(7, edges)
}

fun countComponentsdfs2(n: Int, edges: Array<IntArray>): Int {
    var res = 0

    val adj = Array<ArrayList<Int>>(n) { ArrayList() }
    val visited = BooleanArray(n)
    edges.forEach { edge ->
        adj[edge[0]].add(edge[1])
    }

    var ans = ArrayList<Int>()
    for (i in 0 until n) {
        if (!visited[i]) {
            println(i)
            res++
            ans = dfs3(adj, visited, i)
            println(ans)
        }
    }
    return res
}

fun dfs3(adj: Array<ArrayList<Int>>, isVisited: BooleanArray, vertex: Int): ArrayList<Int> {
    var arr = ArrayList<Int>()
    if (isVisited[vertex]) {
        return arr
    }
    isVisited[vertex] = true
    arr.add(vertex)

    // loop throgh the node
    for (j in 0 until adj[vertex].size) {
        arr.addAll(dfs3(adj, isVisited, adj.get(vertex).get(j)))
//        (dfs3(adj, isVisited, adj.get(vertex).get(j)))
    }
    return arr
}

