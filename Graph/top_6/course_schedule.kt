import java.util.*


internal class Solution515 {
    fun isPossible(V: Int, prerequisites: Array<IntArray>): Boolean {
        // Form a graph
        val adj = ArrayList<ArrayList<Int>>()
        for (i in 0 until V) {
            adj.add(ArrayList())
        }
        val m = prerequisites.size
        for (i in 0 until m) {
            adj[prerequisites[i][0]].add(prerequisites[i][1])
        }
        val indegree = IntArray(V)
        for (i in 0 until V) {
            for (it in adj[i]) {
                indegree[it]++
            }
        }
        val q: Queue<Int> = LinkedList()
        for (i in 0 until V) {
            if (indegree[i] == 0) {
                q.add(i)
            }
        }
        val topo: MutableList<Int> = ArrayList()
        // o(v + e)
        while (!q.isEmpty()) {
            val node = q.peek()
            q.remove()
            topo.add(node)
            // node is in your topo sort
            // so please remove it from the indegree
            for (it in adj[node]) {
                indegree[it]--
                if (indegree[it] == 0) q.add(it)
            }
        }
        return if (topo.size == V) true else false
    }
}

object tUf {
    @JvmStatic
    fun main(args: Array<String>) {
        val N = 4
        val prerequisites = Array(3) { IntArray(2) }
        prerequisites[0][0] = 1
        prerequisites[0][1] = 0
        prerequisites[1][0] = 2
        prerequisites[1][1] = 1
        prerequisites[2][0] = 3
        prerequisites[2][1] = 2
        val obj = Solution515()
        val ans: Boolean = obj.isPossible(N, prerequisites)
        if (ans) println("YES") else println("NO")
    }
}