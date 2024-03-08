package com.hubberspot.dsalgo.graph

import java.util.*

class AdjListGraph( // number of vertices
    private val V: Int
) {
    private val adj = arrayOfNulls<LinkedList<Int>>(V)
    private var E // number of edges
            = 0


    fun dfsIterative(visited: BooleanArray, s: Int) {
        val stack = Stack<Int>()
        stack.push(s)
        while (!stack.isEmpty()) {
            val node = stack.pop()
            if (!visited[node]) {
                visited[node] = true
                print("$node ")
                for (neighbor in adj[node]!!) {

                    if (!visited[neighbor]) {

                        // Do not need to check true again here
                        stack.push(neighbor)
                    }
                }
            }
        }
    }

    init {
        for (v in 0 until V) {
            adj[v] = LinkedList()
        }
    }

    fun addEdge(u: Int, v: Int) {
        adj[u]?.add(v)
        adj[v]?.add(u)
        E++
    }

    override fun toString(): String {
        val sb = StringBuilder()
        sb.append("$V vertices, $E edges \n")
        for (v in 0 until V) {
            sb.append("$v: ")
            for (w in adj[v]!!) {
                sb.append("$w ")
            }
            sb.append("\n")
        }
        return sb.toString()
    }

    fun bfs(s: Int) {
        val visited = BooleanArray(V)
        val q: Queue<Int> = LinkedList()
        visited[s] = true
        q.offer(s)
        while (!q.isEmpty()) {
            val u = q.poll()
            print("$u ")
            for (v in adj[u]!!) {
                if (!visited[v]) {
                    visited[v] = true
                    q.offer(v)
                }
            }
        }
    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val size = 5
            val g = AdjListGraph(size)
            g.addEdge(0, 1)
            g.addEdge(1, 2)
            g.addEdge(2, 3)
            g.addEdge(3, 0)
            // 4
            println(g)

            // Better to pass in a visited array
            var visited = BooleanArray(size)
            // Another way to do this is like in edges before
            for (i in 0 until 5) {
                if (!visited[i]) {
                    g.dfsIterative(visited, i)
                }
            }
        }
    }
}