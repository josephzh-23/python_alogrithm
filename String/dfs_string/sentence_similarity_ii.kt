package Graph.dfs_string

import java.util.HashSet



fun Solution(): Boolean {

    var edges = listOf(
        listOf("great", "fine"),
        listOf("drama", "acting"),
        listOf("skills", "talent")
    )

    // One thing that's very useful to use here is the problem
    //
    var g = mutableMapOf<String, MutableSet<String>>()
    var sentence1 = arrayOf("great", "acting", "skills")
    var sentence2 = arrayOf("fine", "drama", "talent")


    for (edge in edges) {
        // Will get you a
        for (i in edges.indices) {

            var (edge1, edge2) = Pair(edge[0], edge[1])
            g.computeIfAbsent(edge1) { HashSet() }.add(edge2)
            g.computeIfAbsent(edge2) { HashSet() }.add(edge1)
        }
    }

    // Build the graph section
    sentence1.zip(sentence2).forEach {
        var (s1, s2) = Pair(it.first, it.second)
        // Here word1 and word 2 are both found here
        if (!dfsString(s1, s2, g, mutableSetOf())) {
            return false
        }


    }
    return true
    // So basically here is much more clearer here
    // If s2 = "great"
    // and the key is "great" -> "fine" then will be checking the
    // following here

}


// Traverse through all the neighbors of an email say
// Say "john@gmail.com" and all its neighbors here
fun dfsString(
    word1: String,
    word2: String,
    g: MutableMap<String, MutableSet<String>>,
    visited: MutableSet<String>
): Boolean {
    // Check first conditino here

    if (g[word1] == null || g[word1]!!.size == 0) return false

    // We check first if s2 is in s1's negigbors
    if (g[word1]!!.contains(word2)) return true
    g[word1]?.let {
        for (neighbor in it) {

            // We check if s1's neighbor has s2 contained here
            if (visited.contains(neighbor)) continue
            if (dfsString(neighbor, word2, g, visited)) return true
        }
    }
    return false
}