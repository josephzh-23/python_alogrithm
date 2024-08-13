package Array.Basic

internal class DuplicateZeroesSolution {
    fun duplicateZeros(arr: IntArray) {
        var zeroes = 0
        for (i in arr) {
            if (i == 0) {
                zeroes++
            }
        }
        var i = arr.size - 1
        var j = arr.size + zeroes - 1
        while (i != j) {
            insert(arr, i, j--)
            if (arr[i] == 0) {
                insert(arr, i, j--)
            }
            i--
        }
    }

    private fun insert(arr: IntArray, i: Int, j: Int) {
        if (j < arr.size) {
            arr[j] = arr[i]
        }
    }
}