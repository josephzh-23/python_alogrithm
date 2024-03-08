//package Hard
//
//import java.lang.Integer.max
//
//
//fun Tree.Hard.Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main() {
//    var colors = "abaca"
//
//    largestPathValue(colors, arrayOf(intArrayOf(0, 1),
//            intArrayOf(0, 2),
//            intArrayOf(2, 3),
//            intArrayOf(3, 4)))
//}
//
//fun largestPathValue(colors: String, edges: Array<IntArray>): Int {
//    // And then the values here
//    var adj = Array<ArrayList<Int>>(edges.size + 1) { ArrayList() }
//    val visited = BooleanArray(edges.size + 1)
//
//    var n = edges.size + 1
//    // Based on the color dynamically here
//    // 'abcad'
//
//    // For the colors put them in a
//    var maxSize = 0
//
//    // 0-> 1
//    // 0-> 2-> 3-> ->4
//    edges.forEach { edge ->
//
//        adj[edge[0]].add(edge[1])
//    }
//    // Store prev results
//    var tempList = ArrayList<Int>()
//
//    // store the current results
//    var resList = ArrayList<Int>()
//
//    // build a Graph.Edges_question.dfs to capture all the arraylist here
//    for (i in 0 until n) {
//        if (!visited[i]) {
//            //0, 1
//            tempList = resList
//            // 0, 2, 3, 4
//            resList = Graph.Edges_question.dfs(adj, visited, i, ArrayList())
//            print(resList)
//            if (tempList.size > resList.size) {
//                resList = tempList
//            }
//
//        }
//    }
//    var list = mutableListOf<Char>()
//    // a
//    for (i in colors.indices) {
//        if (i == resList[i]) {
//            list.add(colors[i])
//        }
//    }
//    println(list)
//    return 0
//}
//
//fun Graph.Edges_question.dfs(adj: Array<ArrayList<Int>>, isVisited: BooleanArray, vertex: Int,
//        resList: ArrayList<Int>): ArrayList<Int> {
//    if (isVisited[vertex]) {
//        return ArrayList()
//    }
//    resList.add(vertex)
//    isVisited[vertex] = true
//    // loop throgh the node
//    for (j in 0 until adj[vertex].size) {
//        Graph.Edges_question.dfs(adj, isVisited, adj.get(vertex).get(j), resList)
//    }
//    return resList
//}