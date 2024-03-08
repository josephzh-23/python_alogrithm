package Graph.dijkstra;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class path_with_max_probability {

    public double maxProbability(int n, int[][] edges, double[] succProb, int
            start, int end) {

        double[] prob = new double[n];
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
        List<int[]>[] adjList = new ArrayList[n];
        for (int i = 0; i < edges.length; i++) {

            // These 2 should be the opposite here
            adjList[edges[i][0]].add(new int[]{edges[i][1], i});
            adjList[edges[i][1]].add(new int[]{edges[i][0], i});

        }
        prob[start] = 1;
        maxHeap.offer(start);

        while (!maxHeap.isEmpty()) {

            int cur = maxHeap.poll();
            for (int[] nei : adjList[cur]) {
                if (prob[cur] * succProb[nei[1]] > prob[nei[0]]) {
                    prob[nei[0]] = prob[cur] * succProb[nei[1]];
                    maxHeap.offer(nei[0]);
                }
            }
        }


        return prob[end];

    }
}






