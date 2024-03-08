package Sliding_window.Basic

import java.lang.Integer.min

/*

This is the dynamic sliding window here
Say you ahve x= 7
and the array [1, 2, 3, 4, 5, 6] and then
 */

fun answer(arr:List<Int>, x:Int) {
    var minLength = Int.MIN_VALUE

    // Current range and sum of sliding window
    var (start, right, curSum) = intArrayOf(0, 0, 0)

    // Expand window until met
    while(right < arr.size){
        curSum += arr[right]
        right += 1

        // Contract window until no longer meet condition
        while(start < right&& curSum >=x){
            curSum -= arr[start]
            start += 1

            // Update the min Length if shorter
            minLength = min(minLength, right - start + 1)
        }
    }

}