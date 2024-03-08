package Graph.Top_6

import java.util.*

/*
This would look like the following
    0
  1   2
    3
  4   5
     ->   3 1 0 ->   4 3  1 0  ->   pop 4
    5 3  1  0 ->   pop 5 ->
       3  1  0  ->   2 3  1  0 -> pop 2
       3 1 0 -> pop 3       1 0
 */


private class Graph2( //number of nodes
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

    fun DFSUtil(vertex: Int, visited: BooleanArray) {
        visited[vertex] = true //mark the node as explored
        print("$vertex ")
        var a = 0
        for (i in adj[vertex]!!.indices)
        //iterate through the linked list and then propagate to the next few nodes
        {
            a = adj[vertex]!!.get(i)
            if (!visited[a]) //only propagate to next nodes which haven't been explored
            {
                DFSUtil(a, visited)
            }
        }
    }

    fun DFS(v: Int) {
        val already = BooleanArray(V) //initialize a new boolean array to store the details of explored nodes
        DFSUtil(v, already)


    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val g = Graph2(6)
            g.addEdge(0, 1)
            g.addEdge(0, 2)
            g.addEdge(1, 0)
            g.addEdge(1, 3)
            g.addEdge(2, 0)
            g.addEdge(2, 3)
            g.addEdge(3, 4)
            g.addEdge(3, 5)
            g.addEdge(4, 3)
            g.addEdge(5, 3)
            println(
                    "Following is Depth First Traversal: ")
            g.DFS(0)
        }
    }
}