//package Graph.kruskal
//
//import java.util.*
//
//fun numBusesToDestination(routes: Array<IntArray>, source: Int, target: Int): Int {
////    var n = routes.size
////    var g = Array(n) {IntArray(n)}
//
//    var n = routes.size
//    // Use a list of list here, since size is unknown
//
//    val g: MutableMap<Int, MutableList<Int>> = HashMap()
//
//
//    // Make sure it's all sorted
//    for (i in 0 until n) {
//        Arrays.sort(routes[i])
//    }
//
//    for (i in 0 until n) {
//        for (j in i + 1 until n) {
//            // remember to sort the array here
//            if (intersect(routes[i], routes[j])){
//                routes[i].forEach{
//                    var start =
//                    if(!g.containsKey(src))
//                }
//            }
//        }
//    }
//}
//
//
//fun intersect(A: IntArray, B: IntArray): Boolean {
//    var i = 0
//    var j = 0
//    while (i < A.size && j < B.size) {
//        if (A[i] == B[j]) return true
//        if (A[i] < B[j]) i++ else j++
//    }
//    return false
//}