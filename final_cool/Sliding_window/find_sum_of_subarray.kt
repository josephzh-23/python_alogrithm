package final_cool.Sliding_window

import January_3rd.print

// Find the total of the sum of square here right here

// Find the sum of all subarrays of length 3, so if you have array of length
// [1, 2, 3, 4, 5 ,6] and find total of each subarray of length 3 so would become

// 1 + 2 + 3 = 6        and add that up
// 2 + 3 + 4 = 9        adn add that
//

fun main() {
    // Should give 24 here
    val arr = intArrayOf(1, 2, 3,4 , 5)
    findSumSlidingWindow(arr, 2).print()
}
 fun findSumSlidingWindow(arr: IntArray, k : Int): Int{

     // The result of each sliding window right here
     var curRes = 0
     var res = 0


     // Sum up the first subarray and add it to the result here
     for(i in 0 until k){

         curRes+=arr[i]
//         println(res)
     }
     res = curRes
     // To get each subsequent subarray, add the next value in the list
     // remove the first value

     // Start at 1 because 0 is already accounted for, to prevent out of bound
     // exception
    for(i in 1 until arr.size -k +1){
        // Get rid of the old one
        curRes = curRes - arr[i - 1]

        // Add the new one here
        curRes =curRes + arr[i + k -1]
        println(curRes)
        res += curRes
    }
     return res

 }














