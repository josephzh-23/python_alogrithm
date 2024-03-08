//import java.util.*
//
//
//// If using this and then we are given the following code
//fun Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main() {
//    var arr = arrayOf(
//        intArrayOf(1, 2, 3), intArrayOf(0, 2),
//        intArrayOf(0, 1, 3), intArrayOf(0, 2)
//    )
//
//    isBipartite(arr).print()
//}
//// If using this we are given, we can try to do the Graph.Edges_question.dfs of this approach
//// and then
//
///*
//Basically there r 2 colors here
//blue means 1        red means -1        no color = 0
//This prob can be done using the s solution here
// */
//fun Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main() {
//    var s = arrayOf(
//        intArrayOf(1, 2, 3), intArrayOf(0, 2),
//        intArrayOf(0, 1, 3), intArrayOf(0, 2)
//    )
//
//    isBipartite(s)
//}
//
//
//// What would this look like?
////[1, 2 , 3]  then this becomes
//fun isBipartite(g: Array<IntArray>): Boolean {
//    val colors = IntArray(g.size)
//    for (i in g.indices) if (colors[i] == 0) {
//        val q: Queue<Int> = LinkedList()
//        q.add(i)
//        colors[i] = 1
//        while (!q.isEmpty()) {
//
//            val node = q.poll()
//
//            // Here if node = 0     [1, 2, 3]
//            // Since 0 will have node 1, 2, 3 here  they are connected by any case
//
//            for (adjacent in g[node]) {
//                println(adjacent)
//                if (colors[adjacent] == colors[node]) return false
//                // So basically here there is no color yet
//                // So we do sth for it and then change it to sth else
//
//                else if (colors[adjacent] == 0) {
//                    q.add(adjacent)
//                    // The opposite of the other one
//                    colors[adjacent] = -colors[node]
//                }
//
//
//                q.add(i)
//
//                // and then here using the code for the other one
//                colors[i] = 1
//                while (!q.isEmpty()) {
//                    val node = q.poll()
//
//                    println()
//
//                    //basically this becomes
//                    // Say if node == 0
//                    // then g[0] = 1, 2, 3
//                    for (adjacent in g[node]) if (colors[adjacent] == colors[node])
//                        return false else if (colors[adjacent] == 0) {
//                        q.add(adjacent)
//                        colors[adjacent] = -colors[node]
//                    }
//                }
//            }
//            return true
//        }
//    }
//
//}