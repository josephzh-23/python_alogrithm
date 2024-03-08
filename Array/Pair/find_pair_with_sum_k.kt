package Array.Pair

// This is the same as the two sum solution here

// Java program to check if there exists a pair
// in array whose sum results in x.

// Notice below is a brute force solution here
internal object GFG {
    // Function to find and print pair
    fun chkPair(A: IntArray, size: Int, x: Int): Boolean {
        for (i in 0 until size - 1) {
            for (j in i + 1 until size) {
                if (A[i] + A[j] == x) {
                    return true
                }
            }
        }
        return false
    }

    @JvmStatic
    fun main(args: Array<String>) {
        val A = intArrayOf(0, -1, 2, -3, 1)
        val x = -2
        val size = A.size
        if (chkPair(A, size, x)) {
            println("Yes")
        } else {
            println("No")
        }
    }
}

// This code is contributed by umadevi9616