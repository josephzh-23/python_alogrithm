package Graph.dijkstra;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Network_time_delay {

    public int networkDelayTime(int[][] times, int n, int k) {

        // create an adj list of eahc node and its connections


        // We will then keep going after this
        List<List<int[]>> adjList = new ArrayList<>(n + 1);
        for (int i = 0; i < n + 1; i++) {
            adjList.add(null);

        }
        for (int i = 0; i < times.length; i++) {

            int[] edge = times[i];

            int sourceNode = edge[0];
            int destNode = edge[1];
            int time = edge[2];

            List<int[]> neighborNodes = adjList.get(sourceNode);

            if (neighborNodes == null) {

                neighborNodes = new ArrayList<>();
            }

            int[] neighborNode = new int[2];
            neighborNode[0] = destNode;

            neighborNode[1] = time;
            neighborNodes.add(neighborNode);
            adjList.set(sourceNode, neighborNodes);
        }


        // Create an array of min visit time to the each node here
        int[] minimumVisitTimes = new int[n + 1];

        // At the start it's all this here
        Arrays.fill(minimumVisitTimes, -1);
        minimumVisitTimes[k] = 0;

        // Push node unto the queue here
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.add(k);

        // WHie the q has nodes
        while (queue.size() != 0) {

            // Pop node off the q
            int node = queue.remove();

            // For each of the exstiign node, check if the min time to visit
            // from cur node < existing min visit time

            int timeToCurNode = minimumVisitTimes[node];

            List<int[]> neighbors = adjList.get(node);
            for (int[] neighbor : adjList.get(node)) {
                int destNode = neighbor[0];
                int timeToDestNode = neighbor[1];

                if (minimumVisitTimes[destNode] == -1 || timeToCurNode + timeToDestNode <
                        minimumVisitTimes[destNode]) {

                    //
                    minimumVisitTimes[destNode] = timeToCurNode + timeToDestNode;

                    // Push the adjcent node unto the q if the min time was udpated here
                    queue.add(destNode);
                }
            }

        }

        // Find the max visit tiem from all nodes here
        int maxVisitTime = -1;
        for(int i = 1; i < n + 1; i++){
            int visitTime = minimumVisitTimes[i];

            // if one of the visit time is still this, then impossible to reach
            // all the nodes
            if(visitTime == -1){
                return -1;
            }

            if(visitTime > maxVisitTime){
                maxVisitTime = visitTime;
            }
        }
        return maxVisitTime;
    }
}
