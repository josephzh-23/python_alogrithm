package sorting;

import java.util.Arrays;
import java.util.PriorityQueue;

public class minMeetingRooms {

    public int minMeetingRooms(int[][] intervals){

        Arrays.sort(intervals,(int[]a, int[]b )-> (a[0]- b[0]));
        // Basically this will store the ending time of the times below here
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b) -> a-b);
        minHeap.add(intervals[0][1]);

        for(int i = 1; i< intervals.length; i++){

            // If the current start time > the previously stored ending time,
            // then drop the prev ending time
            if(intervals[i][0] >=minHeap.peek()){

                minHeap.poll();
            }
            minHeap.add(intervals[i][1]);

        }
        return minHeap.size();
    }
}
