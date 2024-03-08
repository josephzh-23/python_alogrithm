//import Array.intpair
//import java.util.*
//
//fun Sliding_window.Basic.Sliding_window.Graph.Hard.main() {
//    var edges = arrayOf(intArrayOf(0, 1), intArrayOf(1, 2),
//    intArrayOf(0, 2)
//    )
//
//    val prob = DoubleArray(edges.size)
//
//    // Once the above is given here
//    var success = doubleArrayOf(0.5, 0.5, 0.2)
//    val maxHeap = PriorityQueue<IntArray>()
//    val adjList: MutableMap<Int, ArrayList<Int>> = mutableMapOf()
//    edges.forEachIndexed {it, array->
//        val (start, end) = Pair(array[0], array[1])
//        adjList.computeIfAbsent(start) { ArrayList() }.add(end,success[it].toInt())
//        adjList.computeIfAbsent(end) { ArrayList() }.add(start)
//    }
//
//    // So we add from the start to the end here
//    val minHeap: Queue<IntArray> = PriorityQueue { a:
//                                                   IntArray, b: IntArray -> b[0] - a[0] }
//
//    var (start, end )= intpair(2, 2)
//    val visited = Array(rowSize) { BooleanArray(colSize) }
//
//    // prob, start, end
//    minHeap.add(intArrayOf(0, 0, 0))
//    while(!minHeap.isEmpty()){
//        var (prob, start, end) = minHeap.poll()
//        println("the popped queue is $node")
//
//        // traverse thru the neighbor
//        adjList[start]?.forEach{neigh->
//            println(neigh)
//            if(!visited[neigh]){
//                visited[neigh] = true
//                q.add(neigh)
//            }
//        }
//    }
//
//}