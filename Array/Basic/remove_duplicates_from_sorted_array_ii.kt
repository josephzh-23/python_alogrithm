import tricks.arr
import java.lang.Integer.min

fun removeDuplicatesII(nums: IntArray) {

    var (l, r) = arrayOf(0, 0)

    while (r < nums.size) {
        count = 1

        while (r + 1 < nums.size && nums[r] == nums[r + 1]) {
            r += 1
            count += 1
        }
        for (i in 0 until min(2, count)) {

            // Make sure we can have 1, 1, 1, 2, 2,
            // Make sure we can have 1, 1, 2, 2,
            nums[l] = nums[r]
            l += 1
        }
        r += 1
    }
}