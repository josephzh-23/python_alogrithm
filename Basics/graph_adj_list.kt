package Util

import java.util.*

internal class Graph( //number of nodes
        private val V: Int) {
    private val adj: Array<LinkedList<Int>?> //adjacency list

    init {
        adj = arrayOfNulls<LinkedList<Int>>(V)
        for (i in 0 until V) {
            adj[i] = LinkedList<Int>()
        }
    }

    fun addEdge(v: Int, w: Int) {
        adj[v]?.add(w) //adding an edge to the adjacency list (edges are bidirectional in this example)
    }
}