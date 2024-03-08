//package sorting
//
//
/*

Given an array of meeting time intervals intervals
where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 */
import java.util.*

/*
Because there will be a conflict here between the 2 of them
[ 0  -  30 ]
[ 5 - 10]
 */

var intervals = arrayOf(
        Interval(0, 30),
        Interval(5, 10),
        Interval(15, 20)
)

// here the answer is 2
class Interval(val start: Int, var end:Int)

fun main() {

    // 1. sort meeting by the startring time
    Arrays.sort(intervals) { a, b -> a.start - b.start }

    //Initialize a new min-heap and add the first meeting's ending time
    // to the heap. We simply need to keep track of the ending times as that tells us
    // when a meeting room will get free.
    val minHeap = PriorityQueue<Interval> { a, b->
        a.end - b.end
    }

    minHeap.add(intervals[0])
    for(i in 1 until intervals.size){

        // get the current one and check for conflict here
        val cur = intervals[i]
        val earliest = minHeap.poll()
        // No conflict here case
        if(cur.start >= earliest.end){
            earliest.end = cur.start
            // Conflict here
        }else{
            minHeap.add(cur)
        }

        // Readd it at the end
        minHeap.add(earliest)

        // Re add the
    }

    print(minHeap.size)

}