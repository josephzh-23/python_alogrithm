package Array.Interval

import January_3rd.print
import Util.printList
import Util.printNestedList
import java.lang.Integer.max
import java.lang.Integer.min

/*
Using 2 pointer solutino again here
 */

fun main() {
    var slotA = arrayOf(
        intArrayOf(10, 50), intArrayOf(60, 120),
        intArrayOf(140, 210)
    )

    var slotB = arrayOf(intArrayOf(0, 15), intArrayOf(60, 70))
    println(meetingPlanner(slotA, slotB, 8)?.toList())
}

fun meetingPlanner(slotA: Array<IntArray>, slotB: Array<IntArray>, dur: Int)
        : IntArray? {

    // The solution that we did is not so good did not account for all the cases
    // as said

    // Kind of obviosu here what's going on
    var (pa, pb) = intArrayOf(0, 0)
    while (pa < slotA.size && pb < slotB.size) {
        val intervalA = slotA[pa]
        val intervalB = slotB[pb]

        val end = min(intervalA[1], intervalB[1])
        val start = max(intervalA[0], intervalB[0])
        val curDur = end - start

        // Then the answer is found here
        if (dur <= curDur) {
            return intArrayOf(start, start + end)
        } else {
            if (intervalA[1] < intervalB[1]) {
                pa++
            } else {
                pb++
            }
        }
    }
    return null
}