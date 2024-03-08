package Hard


fun main() {
        var colors = "abaca"

    largestPathValue(colors, arrayOf(intArrayOf(0, 1),
            intArrayOf(0, 2),
            intArrayOf(2, 3),
            intArrayOf(3, 4)))
}
fun largestPathValue(colors: String, edges: Array<IntArray>): Int {
    var res = 0

    var n = edges.size
    val adj = Array<ArrayList<Int>>(n+1) { ArrayList() }
    val visited = BooleanArray(n+1)
    edges.forEach { edge ->
        adj[edge[0]].add(edge[1])
    }

    // Will store the longer of the 2 res list here
    var ans = ArrayList<Int>()
    var tempList = ArrayList<Int>()
    for (i in 0 until n) {
        if (!visited[i]) {
            tempList = ans
            println(i)
            ans = dfs4(adj, visited, i)
            if(ans.size < tempList.size){
                ans = tempList
            }
        }
    }
    println(ans)
    var list = mutableListOf<Char>()
    for (i in colors.indices) {
        if (i == ans[i]) {
            list.add(colors[i])
        }
    }
    println(list)
    return res
}

fun dfs4(adj: Array<ArrayList<Int>>, isVisited: BooleanArray, vertex: Int): ArrayList<Int> {
    var arr = ArrayList<Int>()
    if (isVisited[vertex]) {
        return arr
    }
    isVisited[vertex] = true
    arr.add(vertex)

    // loop throgh the node
    for (j in 0 until adj[vertex].size) {
        arr.addAll(dfs4(adj, isVisited, adj.get(vertex).get(j)))
//        (dfs3(adj, isVisited, adj.get(vertex).get(j)))

        // The following will not work
    }
    return arr
}