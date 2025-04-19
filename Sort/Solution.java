package sorting;

import java.util.Arrays;
import java.util.PriorityQueue;


// This is the solution right here very interesting development here
class Solution333 {
    public int mostBooked(int n, int[][] meetings) {
        // sort rooms by start time
        Arrays.sort(meetings, (m1, m2) -> m1[0] - m2[0]);

        // key: int[end time, room number]
        // sort by end time, if the same end time - sort by lowest room number
        PriorityQueue<int []> sheduler = new PriorityQueue<>((m1, m2) ->
                m1[0] == m2[0] ? m1[1] - m2[1] : m1[0] - m2[0]);
        PriorityQueue<Integer> availableRooms = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            availableRooms.add(i); // add all rooms to availability
        }
        
        int[] roomUsageCount = new int[n];
        for (int[] meeting : meetings) {
            int currMeetingStartTime = meeting[0];
            while (!sheduler.isEmpty() && currMeetingStartTime >= sheduler.peek()[0]) { // empty past meetings
                availableRooms.add(sheduler.remove()[1]); // add freed room to availability
            }
            int delay = 0;
            if (availableRooms.size() == 0) { // all rooms are full
                int[] endedMeeting = sheduler.remove();
                delay = endedMeeting[0] - currMeetingStartTime; // add delay
                availableRooms.add(endedMeeting[1]); // add free room back to availability
            }
            int currMeetingEndTime = meeting[1] + delay;
            int availableRoom = availableRooms.remove(); // get lowest available room
            sheduler.add(new int[] {currMeetingEndTime, availableRoom}); // add current meeting 
            roomUsageCount[availableRoom]++;
        }
        
        // find the most used room
        int maxUsedRoom = 0;
        int maxUsage = 0;
        for (int i = 0; i < n; i++) {
            if (roomUsageCount[i] > maxUsage) {
                maxUsage = roomUsageCount[i];
                maxUsedRoom = i;
            }
        }
        return maxUsedRoom;
    }
}