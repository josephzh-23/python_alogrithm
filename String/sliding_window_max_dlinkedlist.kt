package String

import java.util.*


/*
1.Check Any el out of bound
2. Any el <= a[i]
If el < a[i], then el has to be removed. This is why it’s stored in decreasing fashion, can be
removed in from the back here.

3. Then also add the last element to this as well
4. Add the results to the results array with the index and the value at that index

 5. Can remove from the back here
 */

internal object TUF {
    fun maxSlidingWindow(a: IntArray, k: Int): IntArray {
        val n = a.size

        // this would be size of the sldingind window
        val r = IntArray(n - k + 1)

        // store right idx, this is for
        var rightIndex = 0

        // store index of the elements, not the values
        // itself
        val q: Deque<Int> = ArrayDeque()
        for (i in a.indices) {

            // remove numbers out of range k
            if (!q.isEmpty() && q.peek() == i - k) {
                q.poll()
            }
            // remove smaller numbers in k range as they are useless
            while (!q.isEmpty() && a[q.peekLast()] < a[i]) {
                q.pollLast()
            }

            // Now add to back the new index at each level
            q.offer(i)

            /*
            1, 3, -1      at here when idx = 2, k = 3
            it will start getting the max from the q here
            r[2] = 1
             */
            if (i >= k - 1) {

                r[rightIndex++] = a[q.peek()]
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
        val ans = maxSlidingWindow(arr, k)
        println("Maximum element in every $k window ")
        i = 0
        while (i < ans.size) {
            print(ans[i].toString() + "  ")
            i++
        }
    }
}