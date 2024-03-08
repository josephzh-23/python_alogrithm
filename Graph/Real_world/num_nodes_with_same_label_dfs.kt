package Graph.Real_world

import java.util.*
/*

We gernearlly don't recommend doing things this way it's a lot harder to do it with this


adj[x] contains a set of all the neighbors

counts[node][labels[node] - 'a']
    - storing the count of each node here

 Also, check if node is a leaf node.
 It is a leaf node, if node != 0 && adj[node].size() == 1. Push node into the queue.

How to determine when we get to a parent
1.  We remove node from adj[parent] to avoid traversing back to node from parent
2. add counts[node] to counts[parent]

3. if adj[parent].size ==1 && parent != 0  (root has no parent)
 */

internal class Solution {
    internal inner class Element(var id: Int, var parent: Int)

    fun countSubTrees(n: Int, edges: Array<IntArray>, labels: String): IntArray {
        val graph = buildGraph(edges)
        val stack: Deque<Element> = ArrayDeque()
        val nextNodeToVisit = IntArray(n)
        val result = IntArray(n)
        val nodesToCounts = Array(n) { IntArray(26) }
        val visited = BooleanArray(n)
        stack.push(Element(0, -1))
        while (!stack.isEmpty()) {
            val curNode = stack.peek().id
            val parent = stack.peek().parent
            visited[curNode] = true
            val neighbors: List<Int> = graph[curNode] ?: ArrayList()
            for (neighbor in neighbors) {
                if (parent == neighbor) {
                    continue
                }
                    val nextNode = neighbors[nextNodeToVisit[curNode]]
                    if (visited[nextNode]) {
                        nextNodeToVisit[curNode]++
                        continue
                    }
                    stack.push(Element(nextNode, curNode))
                    break
                    nextNodeToVisit[curNode]++
                }
                if (nextNodeToVisit[curNode] == neighbors.size) {
                    val curLabel = labels[curNode].toInt() - 'a'.toInt()
                    val curCounts = nodesToCounts[curNode]
                    curCounts[curLabel]++
                    result[curNode] = curCounts[curLabel]
                    if (parent != -1) {
                        for (i in curCounts.indices) {
                            nodesToCounts[parent][i] += curCounts[i]
                        }
                    }
                    stack.pop()
                }
            }
            return result
        }

        private fun buildGraph(edges: Array<IntArray>): Map<Int, MutableList<Int>> {
            val graph: MutableMap<Int, MutableList<Int>> = HashMap()
            for (edge in edges) {
                val from = edge[0]
                val to = edge[1]
                graph.computeIfAbsent(from) { ArrayList() }.add(to)
                graph.computeIfAbsent(to) { ArrayList() }.add(from)
            }
            return graph
        }
    }