package String

import java.util.HashMap

/*
The window size here would be n - k + 1
 */

fun main() {
var arr = intArrayOf(1, 5, 9, 3, 3, 7, 3)
    distinctElements(arr, 3).forEach{
        println(it)
    }
}

fun distinctElements(arr: IntArray, k: Int): List<Int> {
    val results: MutableList<Int> = ArrayList()
    val elemCountMap: MutableMap<Int, Int> = HashMap()
    val len = arr.size

    // Create a first window nad put all the elements and its count of this window
    // in a hashmap here
    for (j in 0 until k) {
        elemCountMap[arr[j]] = elemCountMap.getOrDefault(arr[j], 0) + 1
    }
    results.add(elemCountMap.size)
    for (j in 1..len - k) {
        val removeElem = arr[j - 1]
        val addElem = arr[j + k - 1]

        // remove elem from the map
        removeElemFromMap(elemCountMap, removeElem)

        // Add elem from the map here
        elemCountMap[addElem] = elemCountMap.getOrDefault(addElem, 0) + 1
        results.add(elemCountMap.size)
    }
    return results
}

// Either decrease the count by 1 or remove completely here
private fun removeElemFromMap(elemCountMap: MutableMap<Int, Int>, elem: Int) {
    val count = elemCountMap[elem]
    if (count != null && count > 1) {
        elemCountMap[elem] = count - 1
    } else {
        elemCountMap.remove(elem)
    }
}
