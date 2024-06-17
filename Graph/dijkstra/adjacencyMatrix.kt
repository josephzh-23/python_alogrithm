package Graph.Top_6


class GraphAjdacencyMatrix(var vertex: Int) {
    var matrix: Array<IntArray>

    init {
        matrix = Array(vertex) { IntArray(vertex) }
    }

    fun addEdge(source: Int, destination: Int) {
        //add edge
        matrix[source][destination] = 1

        //add bak edge for undirected graph
        matrix[destination][source] = 1
    }

    fun printGraph() {
        println("Graph: (Adjacency Matrix)")
        for (i in 0 until vertex) {
            for (j in 0 until vertex) {
                print(matrix[i][j].toString() + " ")
            }
            println()
        }
        for (i in 0 until vertex) {
            print("Vertex $i is connected to:")
            for (j in 0 until vertex) {
                if (matrix[i][j] == 1) {
                    print("$j ")
                }
            }
            println()
        }
    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val graph = GraphAjdacencyMatrix(5)
            graph.addEdge(0, 1)
            graph.addEdge(0, 4)
            graph.addEdge(1, 2)
            graph.addEdge(1, 3)
            graph.addEdge(1, 4)
            graph.addEdge(2, 3)
            graph.addEdge(3, 4)
            graph.printGraph()
        }
    }
}