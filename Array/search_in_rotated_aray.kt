package Array

import Binary_search.binarySearch


typealias intpair = Pair<Int, Int>
typealias charpair = Pair<Char, Char>
/*
Perform a binary search to locate the pivot element by
initializing the boundaries of the searching space as left = 0 and
right = n - 1. While left < right:


Let mid = left + (right - left) // 2.
If nums[mid] > nums[n - 1], this suggests that pivot is located to the right of mid,
 hence we set left = mid + 1. Otherwise, pivot could be either at mid or to the left of mid,
  in which case we should set right = mid - 1.
*/

fun sol():Int{
    var target = 4
    var s = intArrayOf(4, 5, 6, 7, 0, 2)

    // Use a 2 pter aprpoach first
    var (left, right) =intpair(0, s.size - 1)

    // Allow you to find index of the pivot element (aka the smallest element)
    while (left <= right) {
        val mid: Int = (left + right) / 2
        if (s.get(mid) > s.get(s.size - 1)) {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }


    // Binary search over elements on the pivot element's left

    // Binary search over elements on the pivot element's left
    val answer: Int = binarySearch(s, 0, left - 1, target)
    return if (answer != -1) {
        answer
    } else binarySearch(s, left, s.size - 1, target)

    // Binary search over elements on the pivot element's right

    // Binary search over elements on the pivot element's right
}

