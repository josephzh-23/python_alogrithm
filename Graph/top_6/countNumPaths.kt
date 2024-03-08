package Graph.Top_6

import java.util.*
import kotlin.collections.HashMap

// Again this is for undirected bidrcctional graph as indicated
// https://leetcode.com/problems/find-if-path-exists-in-graph/


// This is based on checkIfPathValid problem leetcode
// Based on this problem leetcode we have the following

private var edges = arrayOf(intArrayOf(0,1),
        intArrayOf(1, 2),
        intArrayOf(2, 0))
/*

Here will implement the bfs or Graph.Edges_question.dfs approach here

Check if path exists here between 2 nodes
can be solved using bfs or Graph.Edges_question.dfs
 */
fun countNumPath(n: Int, edges: Array<IntArray>, source: Int, destination: Int): Boolean {

    var count = 0
    val g: MutableMap<Int, MutableList<Int>> = HashMap()
    edges.forEach{(a, b)->run{
        g.computeIfAbsent(a) { a -> mutableListOf() }.add(b)
        g.computeIfAbsent(b) { b -> mutableListOf() }.add(a)
    }}

    // Store all the nodes to be visited in q
    var q = LinkedList<Int>()
    var visited = BooleanArray(g.size)

    q.offer(source)

    while(!q.isEmpty()){
        var node = q.pop()
        println("the popped queue is $node")


        if(node == destination){
            return true
        }
        // traverse thru the neighbor of current node
        g.get(node)?.forEach{neigh->
            println(neigh)
            if(!visited[neigh]){
                visited[neigh] = true
                q.add(neigh)
            }
        }
    }

    return false
}

fun main() {
    countNumPath(3, edges, 0, 2)
}