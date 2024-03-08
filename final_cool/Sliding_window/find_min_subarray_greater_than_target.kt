package final_cool.Sliding_window

import java.lang.Integer.min


// The dynamic sliding window
// Minimum length subarray sum question
fun find_min_subarray_greater_than_target(arr:IntArray, tar: Int):Int {

    var minlen = -Int.MIN_VALUE
    var (start, end, curSum) = intArrayOf(0,0,0)

    // extend the sliding window if hit
    while(end< arr.size){

        curSum = curSum +arr[end]

        // Always expand the window at back
        end = end + 1

        // Shrink the window until it
        while (start < end && curSum >= tar){
            curSum = curSum- arr[start]
            start = start + 1

            // update the min lenght if this is shorter  then the current
            // min
            minlen = min(minlen, end- start + 1)
        }

    }
    return minlen
}








