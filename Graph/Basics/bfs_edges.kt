package Graph.Basics

import java.util.*


// Remember in the Graph.Edges_question.dfs case, we used a list here

// O(V + E)
fun main() {

    bfsGraph(null, 2)


}
// O (V + E)
fun bfsGraph(data: Array<IntArray>?, start: Int): Int {

    // Step 1 turn 2d into list first and then go from there
    val times1 = arrayOf(
            intArrayOf(2, 1),
            intArrayOf(2, 3),
            intArrayOf(3, 4)
    );
    val graph: MutableMap<Int, MutableList<Int>> = HashMap()

    // and using the above we have
    //graph.put(1, [1, 2, 3, ])
    times1.forEach{time->
        var src = time[0]
        var tar = time[1]

        // If not contain, then init a new list
        if (!graph.containsKey(src)) {
            graph[src] = LinkedList()
        }
        graph[src]?.add(tar)
    }
    // Now unto the q and set
    var q = LinkedList<Int>()
    val visited = BooleanArray(10)

    // You add the starting point to this
    q.add(start)
    visited[start] = true
    while(!q.isEmpty()){
        var node = q.pop()
        println("the popped queue is $node")

        // traverse thru the neighbor
        graph[node]?.forEach{neigh->
            println(neigh)
            if(!visited[neigh]){
                visited[neigh] = true
                q.add(neigh)
            }
        }
    }

    return 0
}
