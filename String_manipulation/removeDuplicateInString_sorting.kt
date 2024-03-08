import java.util.*

object GFG4 {

    // This one no changing the array here
    /* Method to remove duplicates in a sorted array */
    fun removeDupsSorted(str: String): String {
        var str = str
        var res_ind = 1
        var ip_ind = 1

        // Character array for removal of duplicate characters
        val arr = str.toCharArray()

        /* In place removal of duplicate characters*/
        while (ip_ind != arr.size) {

            // ab   not the same so using this can store
            if (arr[ip_ind] != arr[ip_ind - 1]) {

                // this doesn't change the size of the array
                arr[res_ind] = arr[ip_ind]
                res_ind++
            }
            ip_ind++
        }
        str = String(arr)
        return str.substring(0, res_ind)
    }

    /* Method removes duplicate characters from the string
       This function work in-place and fills null characters
       in the extra space left */
    fun removeDups(str: String): String {
        // Sort the character array
        var str = str
        val temp = str.toCharArray()
        Arrays.sort(temp)
        str = String(temp)

        // Remove duplicates from sorted
        return removeDupsSorted(str)
    }

    // Driver Method
    @JvmStatic
    fun main(args: Array<String>) {
        val str = "geeksforgeeks"
        println(GFG4.removeDups(str))
    }
}