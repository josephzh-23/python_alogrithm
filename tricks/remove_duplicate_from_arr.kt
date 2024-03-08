package tricks

// Remove duplicate form array using O(1) complexity

// Can be done using 2 pointer approach 
fun removeDuplicates(nums: IntArray): Int {
    var insertIndex = 1
    for (i in 1 until nums.size) {
        // We skip to next index if we see a duplicate element
        if (nums[i - 1] != nums[i]) {
            /* Storing the unique element at insertIndex index and incrementing
               the insertIndex by 1 */
            nums[insertIndex] = nums[i]
            insertIndex++
        }
    }
    return insertIndex
}