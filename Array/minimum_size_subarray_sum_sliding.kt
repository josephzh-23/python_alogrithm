import January_3rd.print

// Another sliding window here

/*
The 2 window that sums to 7
 2  3  1   2  4   3
       [      ]
 2  3  1   2  4   3
              [   ]

  When curSum >= target, we do curSum -= num[start]
  when curSum < target, we keep adding curSum += num[end]
 */

fun main() {
    var nums = intArrayOf(2, 3, 1, 2, 4, 3)
    var target = 7
    answer4(nums, target).print()
}

//
fun answer4(nums: IntArray, target: Int): Int {
    var window = Integer.MAX_VALUE
    var size = nums.size
    // Current range and sum of sliding window
    var (start, right, curSum) = intArrayOf(0, 0, 0)

    for (end in 0 until size) {
        curSum += nums[end]
        while (curSum >= target) {
            window = Math.min(window, end - start + 1)
            curSum -= nums[start]
            start++
        }
    }
    return if (window == Int.MAX_VALUE) 0 else window

}