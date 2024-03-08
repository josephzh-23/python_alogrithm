package Recursion


// This works on calculating the remaining sum
// after a deduction here
fun main() {
    // Check if you can find sum in the given array
    var arr = intArrayOf(1, 2, 3, 4)
    calcRemainSum(arr, 0)
}

fun calcRemainSum(arr: IntArray, index: Int) {

    // Sum in both subsets are equal here

    var index = index
    if (index < arr.size) {
        println(arr[index])
        calcRemainSum(arr, index + 1)
    }
    return

}