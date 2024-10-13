/*
This is basically a binary search problem


 */

fun binarySearch2(arr: IntArray, l: Int, r: Int): Int {
    var left = l
    var right = r
    while (left <= right) {
        val mid = left + (right - left) / 2
        // left neighbor greater here
        if (arr[mid] < arr[mid - 1]) {
            right = mid - 1
            // right neighbor is greater here
        } else if (arr[mid] < arr[mid + 1]) {
            left = mid + 1
        } else {
            return mid
        }
    }
    return left
}