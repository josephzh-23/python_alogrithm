package Binary_search

// Begin with mid elem,
// Java implementation of recursive Binary Search
// TC: O(logn)
internal class BinarySearch {
    // Returns index of x if it is present in arr[l..
    // r], else return -1
    fun binarySearch(arr: IntArray, start: Int, end: Int, target: Int): Int {
        var start = start
        var end = end
        val mid = start + (end - start) / 2

        if (start <= end) {
            if (arr[mid] == target) return mid

            // Target on the left side
            if (target < arr[mid]) {
                end = mid - 1
                return binarySearch(arr, start, end, target)

                // target on the right side
            } else {
                start =mid + 1
                return binarySearch(arr, start, end, target)
            }
        }
        return -1
    }

    companion object {
        // Driver method to test above
        @JvmStatic
        fun main(args: Array<String>) {
            val ob = BinarySearch()
            val arr = intArrayOf(2, 3, 4, 10, 40)
            val n = arr.size
            val x = 10
            val result = ob.binarySearch(arr, 0, n - 1, x)
            if (result == -1) println("Element not present") else println("Element found at index "
                    + result)
        }
    }
}
/* This code is contributed by Rajat Mishra */