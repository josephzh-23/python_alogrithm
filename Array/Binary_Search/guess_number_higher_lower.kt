package Binary_search

fun main() {

    // And then here we have

    // And here we will continue to guess the number here


}
// And here good b/c binary search is used here

fun guessNumber(n: Int): Int {
    var low = 1
    var high = n
    while (low <= high) {
        val mid = low + (high - low) / 2
        val res: Int = guessNumber(mid)
        if (res == 0) return mid else if (res < 0) high = mid - 1 else low = mid + 1
    }
    return -1
}