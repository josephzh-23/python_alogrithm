package Two_array

import java.util.*

// Can also be done using the hashmap her e

fun main() {
    val nums1 = intArrayOf(1, 2, 2, 1)
    val nums2 = intArrayOf(2, 2)

    // What if we use sorting to do this question
    Arrays.sort(nums1)
    Arrays.sort(nums2)

    // The k pointer will
    var (i ,j , k) = IntArray(3){0}
    while( i < nums1.size && j < nums2.size){
        if(nums1[i] < nums2[j]){
            i++
        }else if(nums1[i] > nums2[j]){
            j++
        }else{
            nums1[k] = nums1[i]
            i++
            j++
        }
    }
    // Then return the array 1 here
}