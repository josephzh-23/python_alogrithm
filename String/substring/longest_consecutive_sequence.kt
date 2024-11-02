package String

import java.lang.Integer.max

// Given an unsorted array of integers nums,
// return the length of the longest consecutive elements sequence.

// Write sth that runs in O(n) time
fun main() {

    // Longest here [1, 2, 3,4]
    // [ 1, 3, 4, 1 ,3 , 4]
    // 2 pters
    // the one that comes after
    var numsArray = intArrayOf(100, 4, 200, 1, 3, 2)
    longestConsecutive(numsArray)
}

// Then use the value here
fun longestConsecutive(nums: IntArray): Int {
    // 1 ,2,3 , 4

    var longest = 0
    val numSet = HashSet<Int>()

    // add all the numbers to the set first
    var start = 0
    numSet.addAll(nums.toTypedArray())
    nums.forEach { n ->

        // n could be 4, and so we check if 3 is there
        // check if its the start of a sequence

        // so if 3 not before 4, this is the start of sequence
        if (!numSet.contains(n - 1)) {
            var length = 0
            start = 1

            // CHeck if the next consec num in here
            // as mentioned
            while (numSet.contains(n + length)) {
                length++
            }
            longest = max(length, longest)


        }

    }
    return longest
}
