//
//
////https://leetcode.com/problems/redundant-connection/description/
internal class Solution17 {
    fun findRedundantConnection(edges: Array<IntArray>): IntArray? {
        val m = edges.size
        val map: MutableMap<Int, MutableSet<Int>> = HashMap()
        for (i in 1..m) {
            map[i] = HashSet()
        }
        for (edge in edges) {
            if (dfs(HashSet(), map, edge[0], edge[1])) return edge
            map[edge[0]]!!.add(edge[1])
            map[edge[1]]!!.add(edge[0])
        }
        return null
    }

    private fun dfs(visited: MutableSet<Int>, map: Map<Int, MutableSet<Int>>,
                    src: Int, target: Int): Boolean {
        // A redundant connection has been found
        if (src == target) return true
        visited.add(src)
        for (next in map[src]!!) {
            if (!visited.contains(next)) {
                if (dfs(visited, map, next, target)) return true
            }
        }
        return false
    }
}