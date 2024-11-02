package Array


fun main() {
    var singleArr = intArrayOf(1, 2, 3,4, 5)
    rotate(singleArr, 3)
}
// O (n* k)
// Trick do an outer loop around the array   for (i in 0 until k) {
// and then do a swap around the elem
fun rotate(nums: IntArray, k: Int) {
    // speed up the rotation
    var k = k
    k %= nums.size
    println(k)
    var temp: Int
    var previous: Int
    for (i in 0 until k) {
        previous = nums[nums.size - 1]
        for (j in nums.indices) {
            temp = nums[j]
            nums[j] = previous
            previous = temp
        }
    }
}