package Util

fun main() {
    val V = 5
    val adj = ArrayList<ArrayList<Int>>()
    for (i in 0 until V) {
        adj.add(ArrayList())
    }
// edge 0---1
    adj[0].add(1)
    adj[1].add(0)

}