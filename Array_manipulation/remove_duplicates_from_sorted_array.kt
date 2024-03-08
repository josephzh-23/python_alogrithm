package Array_manipulation

import Util.printArray


fun main() {

    var arr = intArrayOf(1, 1, 2)
    removeDuplicates(arr)
}

// Again this is sorted as well
// Again use the 2 pointer approach keep a track of the inserted position

private fun removeDuplicates(nums: IntArray): Int {
    var insertIndex = 1
    for (i in 1 until nums.size) { // We skip to next index if we see a duplicate element
        if (nums[i - 1] != nums[i]) {/* Storing the unique element at insertIndex index and incrementing
                   the insertIndex by 1 */
            nums[insertIndex] = nums[i]
            insertIndex++
        }
    }
    printArray(nums)
    return insertIndex
}