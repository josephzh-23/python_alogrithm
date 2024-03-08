/*



 */

fun main() {
    var arr = intArrayOf(2, 2, 2, 2, 2,5, 5, 5, 8)
}
fun numOfSubarrays(arr: IntArray, k: Int, threshold: Int): Int {
    var res = 0
    var sum = 0
    var curSum = arr.slice(0..k - 1).sum()

    for (i in 0 until arr.size - k + 1) {
        curSum += arr[i + k - 1]
        if ((curSum / k) >= threshold) {
            res++
        }
        curSum -= arr[i]
    }
    return res
}







