package Recursion

fun main() {
    var arr = intArrayOf(1, 2, 3, 4)
    forLoop(arr, 0)
}

fun forLoop(nums: IntArray, i: Int){
    if(i< nums.size){
        println(i)
        forLoop(nums, i+1)
    }
    return
}