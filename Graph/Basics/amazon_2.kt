//package Graph.Basics
//
//import java.lang.Math.abs
//
//
//// It has a location
//class Point(var x: Int){
//
//    var arr = arrayListOf<Int>()
//    // var ind
//}
//
//fun suitableLocations(center: Array<Int>, d: Long): Int {
//    var centers = intArrayOf(-2, 1, 0)
//    val n = centers.size
//    var list = mutableListOf<Point>()
//
//    var pointList = mutableListOf<Point>()
//    for (i in -n until n - 1) {
//        var point = Point(i)
//        pointList.add(point)
//    }
//
//    var map = mutableMapOf<Point, MutableList<Int>>()
//   for(point in pointList){
//        map.putIfAbsent(point, ArrayList())
//       map[point]?.addAll(centers.toList())
//   }
//    val visited = mutableSetOf<Int>()
//    list.forEach {
//        if (!visited.contains(it.x)) {
//            dfs(it, visited, it.x)
//        }
//    }
//
//
//}
//
//fun dfs(point: MutableMap<Point, ArrayList<Int>>, isVisited: MutableSet<Int>, vertex: Int) {
//    if (isVisited.contains(vertex)) {
//        return
//    }
//    isVisited.add(vertex)
//    // loop throgh the node same as verticies
//    for (i in 0 until point.values.size) {
//        dfs(point, isVisited, point.values.)
//    }
//}
//
//fun findDistance(x: Int, centerX: Int): Int {
//
//    return abs(x - centerX)
//}