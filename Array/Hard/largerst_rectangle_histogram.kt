package Array.Hard


fun main() {
    var h = intArrayOf(2, 1, 5, 6, 2, 3)
    largestRectangleArea(h)
}

fun largestRectangleArea(h: IntArray?): Int { //Check null condition
    if (h == null || h.size == 0) return 0

    //Initialize variables left and right
    val n = h.size

    // Store the index of the left
    val left = IntArray(n)
    left[0] = -1

    // Store the index of the right
    val right = IntArray(n)
    right[n - 1] = n

    //index of first left bar with height < current bar height -1
    for (i in 1 until n) {

        // Always stores the index that was previously < the curHeight
        var prev = i - 1
        while (prev >= 0 && h[prev] >= h[i]) {

            // Allows you to traverse back to the previous index that's actually smaller
            prev = left[prev]
        }
        left[i] = prev
        println("the left index is ${left[i]}")
    }

    //  //index of first left bar with height < current bar height -1
    for (i in n - 2 downTo 0) {

        // Previous we check if the height[prev] >= cur height
        // then prev
        var prev = i + 1
        while (prev < n && h[prev] >= h[i]) {
            prev = right[prev]
        }
        right[i] = prev
    }


    var maxArea = 0
    for (i in 0 until n) {
        maxArea = Math.max(maxArea, h[i] * (right[i] - left[i] - 1))
    }
    return maxArea
}