package Util
// When given 3 array values
fun minimumCost(n: Int, connections: Array<IntArray>): Int {
    // this is an array of arrays here
//    val g = Array(n) { IntArray(n) }
    // this is a 2d array here
    val g = Array(n) { IntArray(n) }
    for (f in connections) {
        g[f[0]][f[1]] = f[2]
    }
    return 0
}