package Recursion

// Using recursion here to solve dynamic programming here

fun uniquePaths(m: Int, n: Int): Int {


    // If it's the first row and the first column then
    // the value would be 1 as said
    return if (m == 1 || n == 1) {
        1

    } else uniquePaths(m - 1, n) + uniquePaths(m, n - 1)
}