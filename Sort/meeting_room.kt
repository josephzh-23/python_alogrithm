package sorting

import January_3rd.print
import java.util.*



// O(n)log(n)
// start and the end time here
fun main() {
    var meet = arrayOf(
        intArrayOf(0, 30), intArrayOf(5, 10),
        intArrayOf(15, 20)
    )
    canAttendMeetings(meet).print()
}

fun canAttendMeetings(intervals: Array<IntArray>): Boolean {
    // Chekc if you can attend all the meetigngs

    Arrays.sort(intervals) { a, b -> a[0] - b[0] }

    for (i in 0 until intervals.size) {

        // End of the first one bigger than end of the 2nd here
        if (intervals[i][1] > intervals[i + 1][0]) {
            return false
        }

    }
    return true
}