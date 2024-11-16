package String.Basic



'''
Given a non-empty array of integers nums, every element appear
s twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and
 use only constant extra space.

Input: nums = [2,2,1]
Output: 1
'''
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