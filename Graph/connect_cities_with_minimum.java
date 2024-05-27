package Graph.cool_problems;

import java.util.Arrays;

/*
n order to obtain the MST using Kruskal's algorithm,

1. Sort all the edges
we first sort all the connections (edges) present in the graph based on their weights
(in increasing order) and will iterate over them one by one.

2. Based on the union
 Each time we find a new edge which does not result in a cycle with the
 edges selected so far (where we can do a union)
  we add that edge in the final MST and we add the cost for it.
   We keep doing this till we have obtained the MST which connects all the nodes in the graph (i.e.
   connects all the cities using the connections).

3.
 */
public class connect_cities_with_minimum {

    public int minimumCost(int n, int[][] connections){

        Arrays.sort(connections, (a, b) -> a[2] - b[2]);
        int[] parent = new int[n+1];

        int[] rank = new int[n+1];

        // Make each one its own parent here
        for(int i = 1; i<=n; ++i)
            parent[i] = i;
        int cost = 0;

        /*
        The num edges here can only hit n -1 at the biggest
         */
        int num_edges = 0;

        // For each connection union them
        for(int [] connection: connections){
            // If can join them in the same union then can do
            // If you can do a union meaning what
            if(union(parent, rank, connection[0], connection[1])){
                cost += connection[2];
                ++num_edges;
            }
        }

        return num_edges == n-1 ? cost: -1;
    }

    private boolean union(int[] parent, int[] rank, int x, int y){
        int rootX = find(parent, x);
        int rootY = find(parent, y);
        if(rootX == rootY)return false;

        if(rank[rootX] > rank[rootY]){
            parent[rootY] = rootX;
        }else if(rank[rootX] > rank[rootY]){
            parent[rootX] = rootY;
        }else{
            parent[rootY] = rootX;
            ++rank[rootX];
        }
        return true;
    }

    // Path compression of union find here
    // The idea is to make the found ancestor of parent of x
    // so this way no need to traverse all intermiediate nodes again
    private int find(int[] parent, int x){
        if(parent[x] == x)
            return x;
        parent[x] = find(parent, parent[x]);
        return parent[x];
    }
}
