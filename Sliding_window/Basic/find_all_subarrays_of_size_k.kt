package Sliding_window.Basic

// This reduces the TC from O(n*k) down to O(n)
fun fixedSlidingWindow(arr: IntArray, k: Int): MutableList<Int> {
// Sum up the first subarray and then add to the result here
    var curSubArray = 0
    var n = arr.size
    var result = mutableListOf<Int>()
    result.add(curSubArray)

    // To get each subsequent subarray, add the next value
    // in the list and remove the first value here
    for(i in 1 until n-k ){

        curSubArray -= arr[i - 1]
        // Add the next value outside of the window here
        curSubArray += arr[i + k - 1]
        result.add(curSubArray)
    }
    return result
}