package Sliding_window


import java.util.*

/*
 1. Remember your deque would be kept in decreasing order
 */

internal object TUF33 {
    fun minSlidingWindow(a: IntArray, k: Int): IntArray {
        val n = a.size

        // this would be size of the sldingind window
        val r = IntArray(n - k + 1)

        // store right idx, this is for
        var ri = 0
        // store index of the elements
        val q: Deque<Int> = ArrayDeque()
        for (i in a.indices) {

            // remove numbers out of range k
            if (!q.isEmpty() && q.peek() == i - k) {
                q.poll()
            }
            // remove smaller numbers in k range as they are useless
            while (!q.isEmpty() && a[q.peekLast()] > a[i]) {
                q.pollLast()
            }

            // Now add to back
            q.offer(i)

            /*
            0  1  2     at here when idx = 2, k = 3
            it will start getting the max from the q here
             */
            if (i >= k - 1) {

                r[ri++] = a[q.peek()]
            }
        }
        return r
    }

    @JvmStatic
    fun main(args: Array<String>) {
        var i: Int
        var j: Int
        var n: Int
        val k = 3
        var x: Int
        val arr = intArrayOf(1, 3, -1, -3, 5, 3, 6, 7)
        val ans = minSlidingWindow(arr, k)
        println("Maximum element in every $k window ")
        i = 0
        while (i < ans.size) {
            print(ans[i].toString() + "  ")
            i++
        }
    }
}