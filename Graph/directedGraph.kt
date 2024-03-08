package Graph

/*
When is a directed graph cyclic? A - b - c - d- e - a
this above forms a cyclic graph as said
 */



//class to store edges of the weighted graph
internal class Edge(var src: Int, var dest: Int, var weight: Int)

// Graph class
internal class DirectedGraph(edges: List<Edge>) {
    // node of adjacency list
    internal class Node(var value: Int, var weight: Int)

    // define adjacency list
    var adj_list: MutableList<MutableList<Node>> = ArrayList()

    //Graph Constructor
    init {
        // init a list for each node in adj list
        for (i in edges.indices) adj_list.add(i, ArrayList<Node>())

        // add edges to the graph
        for (e in edges) {
            // allocate new node in adjacency List from src to dest
            adj_list[e.src].add(Node(e.dest, e.weight))
        }
    }

    companion object {
        // print adjacency list for the graph
        fun printGraph(graph: DirectedGraph) {
            var src_vertex = 0
            val list_size = graph.adj_list.size
            println("The contents of the graph:")
            while (src_vertex < list_size) {
                //traverse through the adjacency list and print the edges
                for (edge in graph.adj_list[src_vertex]) {
                    print("Vertex:" + src_vertex + " ==> " + edge.value +
                            " (" + edge.weight + ")\t")
                }
                println()
                src_vertex++
            }
        }
    }
}








