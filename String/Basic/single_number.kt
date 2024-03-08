package String.Basic

import java.util.*

fun main() {
}

// Given a non-empty array of integers nums,
// every element appears twice except for one. Find that single one.
// TC: O(nlogn) here and this is the result here
fun singleNumber(numbers:IntArray):Int{

    // Sort the number if the next and the current not the same then we have found it
    var length = numbers.size
    Arrays.sort(numbers)
    // Once sorted move unto next here
    var i = 0
    while(i < numbers.size -2 ){
        if(numbers[i] != numbers[i + 1]){
            return numbers[i]
        }
    }
    return numbers[i]
}