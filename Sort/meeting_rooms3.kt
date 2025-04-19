package sorting

import java.util.*


/*
Return the number of the room that held the most meetings.
 If there are multiple rooms, return the room with the lowest number.

Solution 2:
If there are no available rooms, the meeting will be delayed until a room becomes free.
 The delayed meeting should have the same duration as the original meeting.

Solution 3:
 1. When a room becomes unused, meetings that have an earlier origina
 l start time should be given the room.
 */


// The TC here is O(n) + O(log n)
internal class Solution33 {
    fun mostBooked(n: Int, meetings: Array<IntArray>): Int {
        // sort rooms by start time
        Arrays.sort(meetings) { m1: IntArray, m2: IntArray -> m1[0] - m2[0] }

        // key: int[end time, room number]
        // sort by end time, if the same end time - sort by lowest room number
        val busyRoomWithTime = PriorityQueue { m1: IntArray, m2: IntArray ->
            if (m1[0] == m2[0]) m1[1] - m2[1] else m1[0] - m2[0]
        }
        val availableRooms = PriorityQueue<Int>()
        for (i in 0 until n) {
            availableRooms.add(i) // add all rooms to availability
        }
        val roomUsageCount = IntArray(n)

        for (meeting in meetings) {
            val currMeetingStartTime = meeting[0]

            // The current starting time > the previously stored time here
            while (!busyRoomWithTime.isEmpty() && currMeetingStartTime >= busyRoomWithTime.peek()[0]) { // empty past meetings
                availableRooms.add(busyRoomWithTime.remove()[1]) // add freed room to availability
            }

            var delay = 0

            if (availableRooms.size == 0) { // all rooms are full
                val endedMeeting = busyRoomWithTime.remove()
                delay = endedMeeting[0] - currMeetingStartTime // add delay

                availableRooms.add(endedMeeting[1]) // add free room back to availability
            }


            val currMeetingEndTime = meeting[1] + delay
            val availableRoom = availableRooms.remove() // get lowest available room
            busyRoomWithTime.add(intArrayOf(currMeetingEndTime, availableRoom)) // add current meeting
            roomUsageCount[availableRoom]++
        }

        // find the most used room
        var maxUsedRoom = 0
        var maxUsage = 0
        for (i in 0 until n) {
            if (roomUsageCount[i] > maxUsage) {
                maxUsage = roomUsageCount[i]
                maxUsedRoom = i
            }
        }
        return maxUsedRoom
    }
}