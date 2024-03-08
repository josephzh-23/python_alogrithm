package Graph.Edges_question// Actually a Graph.Edges_question.dfs problem here


fun main() {
    var arr = arrayOf(intArrayOf(1, 2), intArrayOf(3), intArrayOf(3)
    , intArrayOf())

    allPathsSourceTarget(arr)
}
fun allPathsSourceTarget(graph: Array<IntArray>): List<List<Int>> {
    val result: MutableList<List<Int>> = ArrayList()
    dfs(graph, 0, graph.size - 1, ArrayList(), result)
    return result
}

fun dfs(graph: Array<IntArray>, node: Int, target: Int, list: ArrayList<Int>, result: MutableList<List<Int>>) {
    // Add current node to the sublist
    list.add(node)
    if (node == target) {
        result.add(list)
        return
    }
    for (child in graph[node]) {
        println(list)
        dfs(graph, child, target, ArrayList(list), result)
    }
}