package Binary_search

fun binarySearch(arr: IntArray, target: Int, l: Int, r: Int): Int {
    var start = l
    var end = r
    var index = Int.MAX_VALUE
    while (start <= end) {
        val mid = start + (end - start) / 2
        if (arr[mid] < target) {
            start = mid + 1
        } else if (arr[mid] > target) {
            end = mid
        } else if (arr[mid] == target) {
            index = mid
            break
        }
    }
    return index
}