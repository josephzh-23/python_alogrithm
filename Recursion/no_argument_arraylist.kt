package Recursion

// Using this
fun main(args: Array<String>) {
    val arr = intArrayOf(2, 3, 1, 4, 4, 5)

    println(findAllIndex2(arr, 4, 0))
}

fun findAllIndex2(arr: IntArray, target: Int, index: Int): ArrayList<Int> {
    val list = ArrayList<Int>()
    if (index == arr.size) {
        return list
    }

    // this will contain answer for that function call only
    if (arr[index] == target) {
        list.add(index)
    }
    // This only gets fired when popping from the call stack
    val ansFromBelowCalls = findAllIndex2(arr, target, index + 1)
    list.addAll(ansFromBelowCalls)
    return list
}