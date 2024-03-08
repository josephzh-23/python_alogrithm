package Graph.Cycle_detection

// Perform a Graph.Edges_question.dfs from 1 to # of nodes
// And check if cycle is formed here

// WHen see node:  mark as visited, traverse

// Calling DFS traversal if that node is unvisited
// call recursive function that checks if its a cycle and returns true

//https://www.youtube.com/watch?v=Y9NFqI6Pzd4&t=822s

fun main(args: Array<String>) {
    val V = 5
    val adj = ArrayList<ArrayList<Int>>()
    for (i in 0 until V) {
        adj.add(ArrayList())
    }
    // edge 0---1
    adj[0].add(1)
    adj[1].add(0)

    // edge 1---2
    adj[1].add(2)
    adj[2].add(1)

    // adge 2--3
    adj[2].add(3)
    adj[3].add(2)

    // adge 3--4
    adj[3].add(4)
    adj[4].add(3)

    // adge 1--4
    adj[1].add(4)
    adj[4].add(1)
    val obj = Solution3()
    val ans: Boolean = obj.isCycle(V, adj)
    if (ans == true) {
        println("Cycle Detected")
    } else {
        println("No Cycle Detected")
    }
}



internal class Solution3 {
    // This is a recursive function
    // parent is the previous node

    // 2 -> 3 -> 6
    // parent[2] = -1
    // parent[3] = 2
    fun checkForCycle(node: Int, parent: Int, vis: BooleanArray, adj: ArrayList<ArrayList<Int>>): Boolean {
//        println("the parent is $parent")
        // mark as visited and check each neighbor
        vis[node] = true
        for (neigh in adj[node]) {
            if (vis[neigh] == false) {
                if (checkForCycle(neigh, node, vis, adj) == true) {
                    return true
                }
                // THis checks for the case where next node is the previous node
                // This is the
                /*
                A cycle would form below
                          3
                       /    \
                    1   -    2
                 */
            } else if (neigh != parent) {

                // We found a back edge
                println("the node is $node and $neigh  ")
                return true

            }
        }
        return false
    }

    // General function here
    fun isCycle(V: Int, adj: ArrayList<ArrayList<Int>>): Boolean {
        val vis = BooleanArray(V)
        for (i in 0 until V) {
            if (vis[i] == false) {
                if (checkForCycle(i, -1, vis, adj)) return true
            }
        }
        return false
    }
}