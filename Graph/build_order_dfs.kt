//package Graph
//
//import Tree.Solution5
//
//
//class build_order_dfs {
//
//    //To make sure ther eis no issue of cycling otherwise the whole thing
//    // WOuld be ruined here
//
//    // What we need to do : mark a node as partial (or is visiting) beofre
//    // we start the bfs on it right here
//
//    // so 3 states: right here COMPLETED, PARTIAL AND BLANK
//
//    private fun dfs(node: Int, adj: ArrayList<ArrayList<Int>>, vis: IntArray, dfsVis: IntArray): Boolean {
//        //check the cycle here
//        vis[node] = 1
//        dfsVis[node] = 1
//        for (neighbor in adj[node]) {
//
//            // If it hasn't been visited then check if there is cycle or not xxx
//            if (vis[neighbor] == 0) {
//                if (!dfs(neighbor, adj, vis, dfsVis) == true) {
//                    return false
//                }
//            }
//            dfsVis[node] = 0
//        }
//        return true
//    }
//
//    fun isCyclic(N: Int, adj: ArrayList<ArrayList<Int>>): Boolean {
//        val vis = IntArray(N)
//        val dfsVis = IntArray(N)
//        for (i in 0 until N) {
//            if (vis[i] == 0) {
//                if (dfs(i, adj, vis, dfsVis) == true) return true
//            }
//        }
//        return false
//    }
//
//
//}
//
//
//
//fun Sliding_window.maining_window.Sliding_window.Graph.Hard.main(args: Array<String>) {
//    val graph = ArrayList<ArrayList<Int>>()
//
//    //Vertex - 0
//    var neighbors = ArrayList<Int>()
//    neighbors.add(1)
//    graph.add(neighbors)
//
//    //Vertex - 1
//    // 1 : [2, 5]
//    neighbors = ArrayList()
//    neighbors.add(2)
//    neighbors.add(5)
//    graph.add(neighbors)
////
////    //Vertex - 2: [1, 3]
////    neighbors = ArrayList()
////    neighbors.add(3)
////    graph.add(neighbors)
////
////    //Vertex - 3: [4]
////    neighbors = ArrayList()
////    neighbors.add(4)
////    graph.add(neighbors)
////
////    //Vertex - 4 : [0, 1]
////    neighbors = ArrayList()
////    neighbors.add(0)
////    neighbors.add(1)
////    graph.add(neighbors)
////
////    //Vertex - 5
////    neighbors = ArrayList()
////    graph.add(neighbors)
//
//    val  V= 3
//
//    // CHeck if node visited and hten here
//    if (Solution5.isCyclic(V, graph)) println("Cycle detected") else println("No cycles detected")
//}