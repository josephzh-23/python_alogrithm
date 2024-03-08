package Backtracking

import java.util.ArrayList
import java.util.HashMap

fun treeDiameter(edges: Array<IntArray>, n: Int, k: Int): Int {

    // create an adj list of eahc node and its connections

    val visited = BooleanArray(edges.size)
    val adj: MutableMap<Int, MutableList<Int>> = HashMap()
    for (i in edges) {// The 2nd value is the price
        adj.computeIfAbsent(
            i[0]
        ) { value: Int? -> ArrayList() }!!
            .add(i[1])
        adj.computeIfAbsent(
            i[1]
        ) { value: Int? -> ArrayList() }!!
            .add(i[0])

    }

    for(i in 0 until n){
        if(!visited[i]){
            dfs(adj, visited, i)
        }
    }
    return 0
}


fun dfs(adj: MutableMap<Int, MutableList<Int>>, isVisited: BooleanArray, vertex: Int) {
    if(isVisited[vertex]){
        return
    }

    if(adj[vertex]?.size ==0){
        return
    }
    isVisited[vertex] = true
    // loop throgh the node same as verticies
    for(i in 0 until adj[vertex]?.size!!){
        dfs(adj,isVisited, adj[vertex]?.get(i)!!)
    }
    isVisited[vertex] = false
}