package Pairs

import January_3rd.print
import java.util.*

fun main() {
    // This finds the k closest points here
    var points = arrayOf(intArrayOf(1, 3), intArrayOf(-2, 2))
    kClosest(points, 1)
}

fun kClosest(points: Array<IntArray>, k: Int) {
    // Store the value and then the index
    var minHeap: Queue<IntArray> = PriorityQueue<IntArray> { a, b ->
        a[0] - b[0]
    }

    points.forEachIndexed { idx, point ->
        var ans = dist(point)
        println("ans is $ans")
        minHeap.add(intArrayOf(ans, idx))
    }

    var res = mutableListOf<IntArray>()
    for(i in 0 until k) {
        // The index that popps out of the
        var (value, idx) = minHeap.poll()

        points[idx].forEach{
          println("the value is $it")
        }
        res.add(points[idx])
    }

    res.forEach{
        println(it.print())
    }



}

// This calcs the distance poitns for you
fun dist(point: IntArray): Int {
    return point[0] * point[0] + point[1] * point[1]
}











