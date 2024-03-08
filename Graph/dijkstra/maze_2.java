package Graph.dijkstra;

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {

    int[][] dirs = new int[][]{{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

    public int shortestDistance(int[][] maze, int[] start, int[] destination) {

        int n = maze.length, m = maze[0].length;
        int[][] dist = new int[n][m];

        for (int i = 0; i < n; i++) {

            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }

        dist[start[0]][start[1]] = 0;
        dijkstra(maze, start, destination, dist);

        return dist[destination[0]][destination[1]] == Integer.MAX_VALUE
                ? -1 : dist[destination[0]][destination[1]];


    }

    public void dijkstra(int[][] maze, int[] start, int[] destination, int[][] dist){

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b)-> (a[2] - b[2]));
        //inde 0 : x , index 1: y, indedx2 : the distance

        int n = maze.length;
        int  m = maze[0].length;

        while(!pq.isEmpty()){
            int[] cur = pq.poll();
            if(cur[0]== destination[0] && cur[1] == destination[1]){
                return;
            }
            for(int[] dir:dirs){
                int x = dir[0] + cur[0], y = dir[1] + cur[1],
                        cur_step = 1;

                while( x >= 0 && y>=0 && x< n && y < m && maze[x][y] ==0){
                    x+= dir[0];
                    y+=dir[1];
                    cur_step++;

                }
                x-=dir[0];
                y-=dir[1];
                cur_step--;

                // If you have sth smaller than the previously store distance then yo uneed to update x
                // it as explained updat ethe distance here if not good enugh as said

                if(dist[cur[0]][cur[1]] + cur_step < dist[x][y]){
                    dist[x][y] = dist[cur[0]][cur[1]] + cur_step;
                    pq.add(new int[]{x, y, dist[x][y]});
                }
            }
        }
    }
}
