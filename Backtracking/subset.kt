// subset problem leetcode
// https://leetcode.com/problems/subsets/
/*
Subset problem leetcode solution

So if given [1, 2, 3]

[[],[1],[2],
[1,2],[3],[1,3],[2,3],[1,2,3]]
 */



fun subsets(nums: IntArray): List<List<Int>>? {
    val resultList: MutableList<List<Int>> = ArrayList()

    // Start backtracking from the beginning
    backtrack(resultList, ArrayList(), nums, 0)
//    println(resultList)
    return resultList
}

// Add to start + 1,
private fun backtrack(resultSets: MutableList<List<Int>>, tempSet: MutableList<Int>,
                      nums: IntArray, start: Int) {
    // Add the set to result set
    resultSets.add(ArrayList(tempSet))

    /*
How the order would go would be
[with added 1]              [1, with added 2]
[1, 2, with added 3]        [1, with added 3]

[with added 2]      [2, with added 3]

[with added 3]
 */

    for (i in start until nums.size) {

        println(tempSet + "with added ${nums[i]}")
        // Case of including the number
        tempSet.add(nums[i])
        // Backtrack the new subset
        backtrack(resultSets, tempSet, nums, i + 1)

        // Case of not-including the number
        tempSet.removeAt(tempSet.size - 1)
//        println("removed is $tempSet with start $start")
    }
}

fun main() {
    var arr = intArrayOf(1, 2, 3)
    subsets(arr)
}