package Graph.dijkstra

import java.util.*


class Graph internal constructor(var V: Int, // V-> no. of vertices & E->no.of edges
                                 var E: Int) {
    // A class to represent a graph edge
    inner class Edge : Comparable<Edge> {
        var src = 0
        var dest = 0
        var weight = 0

        // Comparator function used for
        // sorting edgesbased on their weight
        override operator fun compareTo(compareEdge: Edge): Int {
            return weight - compareEdge.weight
        }
    }

    // A class to represent a subset for
    // union-find
    internal inner class subset {
        var parent = 0
        var rank = 0
    }

    var edge: Array<Edge?> // collection of all edges

    // Creates a graph with V vertices and E edges
    init {
        E = E
        edge = arrayOfNulls(E)
        for (i in 0 until E) edge[i] = Edge()
    }

    // A utility function to find set of an
    // element i (uses path compression technique)
    private fun find(subsets: Array<subset?>, i: Int): Int {
        // find root and make root as parent of i
        // (path compression)
        if (subsets[i]!!.parent != i) subsets[i]!!.parent = find(subsets, subsets[i]!!.parent)
        return subsets[i]!!.parent
    }

    // A function that does union of two sets
    // of x and y (uses union by rank)
    private fun Union(subsets: Array<subset?>, x: Int, y: Int) {
        val xroot = find(subsets, x)
        val yroot = find(subsets, y)

        // Attach smaller rank tree under root
        // of high rank tree (Union by Rank)
        if (subsets[xroot]!!.rank < subsets[yroot]!!.rank) subsets[xroot]!!.parent = yroot else if (subsets[xroot]!!.rank > subsets[yroot]!!.rank) subsets[yroot]!!.parent = xroot else {
            subsets[yroot]!!.parent = xroot
            subsets[xroot]!!.rank++
        }
    }

    // The Backtracking.Tree.Hard.Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main function to construct MST using Kruskal's
    // algorithm
    fun KruskalMST() {
        // This will store the resultant MST
        val result = arrayOfNulls<Edge>(V)

        // An index variable, used for result[]
        var e = 0

        // An index variable, used for sorted edges
        var i = 0
        i = 0
        while (i < V) {
            result[i] = Edge()
            ++i
        }

        // Step 1:  Sort all the edges in non-decreasing
        // order of their weight.  If we are not allowed to
        // change the given graph, we can create a copy of
        // array of edges
        Arrays.sort(edge)

        // Allocate memory for creating V subsets
        val subsets = arrayOfNulls<subset>(V)
        i = 0
        while (i < V) {
            subsets[i] = subset()
            ++i
        }

        // Create V subsets with single elements
        for (v in 0 until V) {
            subsets[v]!!.parent = v
            subsets[v]!!.rank = 0
        }
        i = 0 // Index used to pick next edge

        // Number of edges to be taken is equal to V-1
        while (e < V - 1) {

            // Step 2: Pick the smallest edge. And increment
            // the index for next iteration
            val next_edge = edge[i++]

            val x = find(subsets, next_edge!!.src)
            val y = find(subsets, next_edge.dest)

            // If including this edge doesn't cause cycle,
            // include it in result and increment the index
            // of result for next edge
            if (x != y) {
                result[e++] = next_edge
                Union(subsets, x, y)
            }
            // Else discard the next_edge
        }

        // print the contents of result[] to display
        // the built MST
        println("Following are the edges in "
                + "the constructed MST")
        var minimumCost = 0
        i = 0
        while (i < e) {
            println(result[i]!!.src.toString() + " -- "
                    + result[i]!!.dest
                    + " == " + result[i]!!.weight)
            minimumCost += result[i]!!.weight
            ++i
        }
        println("Minimum Cost Spanning Tree "
                + minimumCost)
    }

    companion object {
        // Driver's Code
        @JvmStatic
        fun main(args: Array<String>) {
        // the point in elder ledSmart
            /* Let us create following weighted graph
                 10
            0--------1
            |  \     |
           6|   5\   |15
            |      \ |
            2--------3
                4       */
            val V = 4 // Number of vertices in graph
            val E = 5 // Number of edges in graph
            val graph = Graph(V, E)

            // add edge 0-1
            graph.edge[0]!!.src = 0
            graph.edge[0]!!.dest = 1
            graph.edge[0]!!.weight = 10

            // add edge 0-2
            graph.edge[1]!!.src = 0
            graph.edge[1]!!.dest = 2
            graph.edge[1]!!.weight = 6

            // add edge 0-3
            graph.edge[2]!!.src = 0
            graph.edge[2]!!.dest = 3
            graph.edge[2]!!.weight = 5

            // add edge 1-3
            graph.edge[3]!!.src = 1
            graph.edge[3]!!.dest = 3
            graph.edge[3]!!.weight = 15

            // add edge 2-3
            graph.edge[4]!!.src = 2
            graph.edge[4]!!.dest = 3
            graph.edge[4]!!.weight = 4

            // Function call
            graph.KruskalMST()
        }
    }
}
// This code is contributed by Aakash Hasija