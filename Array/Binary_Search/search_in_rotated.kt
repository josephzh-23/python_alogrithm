package Search


fun search(nums: IntArray?, target: Int): Int {
    if (nums == null || nums.size == 0) {
        return -1
    }
    var l = 0
    var r = nums.size - 1
    // This will break when @ smallest index
    // [4, 5, 6, 7, 0, 1, 2]
    // This would allow you to find the smallest index in the
    // array based on the above, which would be indx = 4

    while (l < r) {
        val midpoint = l + (r - l) / 2

        // 7 > 2 here
        if (nums[midpoint] > nums[r]) {
            l = midpoint + 1

            // If it belongs to the right since it's smaller
            // so r
        } else {
            r = midpoint
        }
    }

    println(" the $l and $r")
    // Here
    val start = l

    // To start a new b search here
    l = 0
    r = nums.size - 1

    // From the above we get l =4 and r = 4
    //                   s         r
    //                   mid
    //      [4, 5, 6, 7, 0, 1, 2]
    // is 5 > 0?
    if (target >= nums[start] && target <= nums[r]) {
        l = start


    } else {
        println("$l")
        r = start
    }

    // Do a regular binary search on the approriate array
    while (l <= r) {
        val mid = l + (r - l) / 2
        if (nums[mid] == target) {
            return mid
        } else if (nums[mid] < target) {
            l = mid + 1
        } else {
            r = mid + 1
        }
    }
    return -1
}

fun main() {
    var arr = intArrayOf(4, 5, 6, 7, 0, 1, 2)
    search(arr, 5)
}
