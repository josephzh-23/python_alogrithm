package Graph.Island_problems


//https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
// Taken from number of connected components
/*
Basically the idea is that you move in here
        One solution is to use DFS.
        The idea is to give each node a flag to mark whether it has been visited.
         For an unvisited node, we will increment the result by 1,
         And then we traverse the neighboring nodes through the adjacency list and
         mark them as visited.
 */



fun main(){
// following will print 2
    // since 0-1-2      2nd connected: 3-4
    println(countComponentsdfs(5, arrayOf(intArrayOf(0, 1),
            intArrayOf(1, 2),
            intArrayOf(3, 4))))
}
fun countComponentsdfs(n: Int, edges: Array<IntArray>): Int {
    var res = 0

    val adj = Array<ArrayList<Int>>(n){ ArrayList() }
    val visited = BooleanArray(n)
    edges.forEach{edge->
        adj[edge[0]].add(edge[1])
        adj[edge[1]].add(edge[0])
    }

    // edges -> can have 0: [1, 2]
    // second one 3: [4]
    for(i in 0 until n){
        if(!visited[i]){
            res++
            dfs(adj, visited, i)
        }
    }
    return res
}

fun dfs(adj: Array<ArrayList<Int>>, isVisited: BooleanArray, vertex: Int) {
   if(isVisited[vertex]){
       return
   }
    isVisited[vertex] = true
    // loop throgh the node
    for(neigh in adj[vertex]){
        println("$vertex with $neigh")

        dfs(adj,isVisited, neigh)
    }
}

