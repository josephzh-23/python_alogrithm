package Graph

fun main() {

    var ar = arrayOf(intArrayOf(1, 2), intArrayOf(3), intArrayOf(3))

    allPathsSourceTarget(ar)
}

fun allPathsSourceTarget(graph: Array<IntArray>): List<List<Int>> {
    val n = graph.size

    val l: MutableList<MutableList<Int>> =ArrayList()
    graph.forEach{
        l.add(it.toMutableList())
    }


    val visited = BooleanArray(n+1)
//
    for(i in 0 until graph.size){
        if(!visited[i]){
            dfs2(l, visited, i)
        }
    }

    println(l)

    return l
//    for (edge in edges) {
//        val a = graph[-]
//        val b = edge[1]
//        graph.computeIfAbsent(a) { `val`: Int? -> ArrayList() }.add(b)
//        graph.computeIfAbsent(b) { `val`: Int? -> ArrayList() }.add(a)
//    }
}



fun dfs2(adj: MutableList<MutableList<Int>>, isVisited: BooleanArray, vertex: Int) {
    if(isVisited[vertex]){
        return
    }

//    println(vertex)
    isVisited[vertex] = true
    // loop throgh the node same as verticies
    println(adj[vertex].size)
    println(adj)
    for(i in 0 until adj[vertex].size){
        dfs2(adj,isVisited, adj[vertex].get(i))
    }
}