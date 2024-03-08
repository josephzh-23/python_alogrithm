package Graph.Basics

import java.util.*


// This is very effective when given a bunch of edges and then a list of list
// and then you see what would happen here
/*
Graph.Edges_question.dfs adjacency list is best for dealing with edges, add them to a list
would be a lot simpler as said
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

//var arr = intArrayOf(0, 1, 1, 2)
fun main() {
    // this below forms 0 1 2
    var edges = arrayOf(intArrayOf(0, 1),
            intArrayOf(1, 2),
            intArrayOf(2, 3))
    // the passed in n is very important
    dfsTraversal(4, edges)
}

fun dfsTraversal(n: Int, edges: Array<IntArray>) {

    val adj = Array<ArrayList<Int>>(n) { ArrayList() }
    // For the boolean array we need to know # of vertices usually given
    // in the questions
    val visited = BooleanArray(n)
    edges.forEach { edge ->
        adj[edge[0]].add(edge[1])
        adj[edge[1]].add(edge[0])
    }
    for (i in 0 until n) {
        if (!visited[i]) {
            dfs2(adj, visited, i)
        }
    }
}

fun dfs2(adj: Array<ArrayList<Int>>, isVisited: BooleanArray, vertex: Int) {
//    println(adj)
    if (isVisited[vertex]) {
        return
    }
    isVisited[vertex] = true
    // loop throgh the node same as verticies
    for (neigh in adj.get(vertex)) {

        println("the popped node is ${neigh})}")
        dfs2(adj, isVisited, neigh)
    }
}