package Coding_Challenges

import java.util.*


/*


What we need to do: find the 2 closest elemsents (from the 2nd
array) to the picked elem of 1st array.
    - sort 2nd array and use bs search
    - using this find the elem > = the picked element

    Will return the distance
 */
fun findTheDistanceValue(arr1: IntArray, arr2: IntArray, d: Int): Int {
//such that there is not any element
// arr2[j] where |arr1[i]-arr2[j]| <= d.

    // Sort the 2nd array first
    var count = 0
    Arrays.sort(arr2)
    for (i in arr1.indices) {


        //   This give you the index of the element
        //   in 2nd array that’s closes to the arr1[I] value.


        var it = Arrays.binarySearch(arr2, 0, arr2.size, arr1[i])

        println(arr1[i])
        println(it)
        // -1 means this is not in range
        if (it < 0) {
//            println(arr1[i])
//            println(it)
            it = -(it + 1)
        }
        var isIt = false

        if (it < arr2.size && Math.abs(arr2[it] - arr1[i]) <= d) {
            isIt = true

        }

        // calc dist between arr2[] distance to arr1[] dist

        if (it != 0 && Math.abs(arr2[it - 1] - arr1[i]) <= d) {
            isIt = true
        }

        // increment count
        if (!isIt) {
            count++
//            println(count)
        }
    }
    println(count)
    return count
}


fun main(){
    /*
     If pass 8 1 will be returned from Array.binarySearch() there
     since 8 is in the array

     2. if not contained in arr,
     returns (-(insertion point) – 1)
     The insertion point is defined as the point at which
      the key would be inserted into the array, same as
    (-1) * (idx of 1st elem > the current element)

      3. Or the length of the entire array if elem
      not in the array
     */

    var arr1 = intArrayOf(22,3, 4, 5, 8)
    var arr2 = intArrayOf(10, 9, 1, 8)
    findTheDistanceValue(arr1, arr2, 2)
}