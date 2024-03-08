package Dynamic_programming

/*
If there exists a subset whose sum = the given value
1  2   3   5
Check for the subsst that makes the sum

Check 1 digit, then check 2 digit sums here
And then once you check it you get
 */

// This is the source code for all of it and it makes alot of sense

object SubsetSum {
    fun isSubsetExists(arr: IntArray, sum: Int): Boolean {
        if (arr.size == 0) {
            return false
        }
        val mat = Array(arr.size) { BooleanArray(sum + 1) }

        // Basically for the 1st column, all the values will be true
        for (i in arr.indices) {
            mat[i][0] = true
        }

        // Update the column for the first row in dp as said
        for (j in 0..sum) {
            if (j == arr[0]) {
                mat[0][j] = true
            }
        }

        // At every position we need to include or exclude the
        // first item
        for (i in 1 until arr.size) {
            for (sum in 1..sum) {

                // Checking for excluding first, if you excluded the last
                // value meaning the row above then make it true
                // then we include
                if (mat[i - 1][sum]) {
                    mat[i][sum] = true
                } else {

                    /*
                    arr[i] your current value
                    j = your sum, if u r checking for sum = 1
                    your arr[i] = 2, then there is no way you can include
                    2 right
                     */
                    if (sum >= arr[i]) {
                        // This is the formula that we had
                        mat[i][sum] = mat[i - 1][sum - arr[i]]
                    }
                }
            }
        }

        // Return the value at the bottom
        return mat[arr.size - 1][sum]
    }

    @JvmStatic
    fun main(args: Array<String>) {
        val arr = intArrayOf(1, 2, 3, 5)
        val sum = 15
        println(isSubsetExists(arr, sum))
    }
}