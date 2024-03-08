package Graph

import org.apache.poi.hssf.util.HSSFColor.WHITE
import java.util.*
import kotlin.collections.ArrayList
import kotlin.collections.HashMap

fun main(){

    var ans = arrayOf(intArrayOf(1, 0),
        intArrayOf(2, 0), intArrayOf(3, 1), intArrayOf(3, 2))
    BuildOrder2(5).apply{
        findOrder(5, ans)
    }
}

class BuildOrder2(numCourses: Int) {

    lateinit var adjList: MutableMap<Node, MutableList<Node>>
    // The topological order
    val topologicalOrder = mutableListOf<Node>()

    // Boolean to check if a cycle is found here
    var isPossible: Boolean = true

    // We need an extra list for traversing here
    val visited = mutableMapOf<Int, Node>()


    // INitialize everything here
    init{
        for( i in 0 until numCourses){
            visited.put(i, Node(i))
        }
    }

    val nums = IntArray(numCourses)
    fun findOrder(numCourses: Int, prerequisites: Array<IntArray>): IntArray {



        adjList = HashMap()
        // This gets decreased when the destination is visited here


        val possible = true

        // Create the adjacency list representation of the graph
        for (i in prerequisites.indices) {
            val src = prerequisites[i][0]
            val dest = prerequisites[i][1]

            val (srcNode, destNode) = Pair(Node(src), Node(dest))
            val lst: MutableList<Node> = adjList.getOrDefault(srcNode, ArrayList())
            lst.add(destNode)
            adjList[srcNode] = lst

            // Make sure things are added here
        }
        // Start the recursion
        for (i in 0 until numCourses){
            if (visited.get(i)?.state != Node.State.COMPLETE) {
                dfs(visited.get(i)!!)
            }
        }
//        if(possible){
//          topologicalOrder.reverse()
//        }


        topologicalOrder.forEach{
            println(it.digit)
        }
        return intArrayOf()
    }

    private fun dfs(
        node: Node
    ) {

        if (!isPossible) {
            return
        }

        // We are just starign so goes from blank -> partial here
        node.state = Node.State.PARTIAL

        // traversing on the neighbor vertice
        for (neighbor in adjList.getOrDefault(node, ArrayList<Node>())) {

            // Not yet visited
            if (visited.get(neighbor.digit)?.state!= Node.State.COMPLETE) {
                dfs(neighbor)
            } else if (neighbor.state === Node.State.PARTIAL) {
                // An edge to a GRAY vertex represents a cycle
                isPossible = false
            }
        }

        // We can replace and then add again her
        node.state = Node.State.COMPLETE
        visited.replace(node.digit, node)
        topologicalOrder.add(node)
    }

}

class Node(var digit: Int){
    var state = State.BLANK
    enum class State{
        COMPLETE,
        PARTIAL,
        BLANK
    }

    override fun hashCode(): Int {
        return Objects.hash(state, digit)
    }
    @Override
    override fun equals(other: Any?): Boolean {
        return this.state == (other as Node).state && this.digit ==
                (other as Node).digit
    }

}
