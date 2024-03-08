package Util

import java.util.*

fun main(args: Array<String>) {
    val arr = arrayOf("b", "e", "a", "f", "d", "c")
    arr.sort()
    for (x in arr) print("$x  ")
}


// Main class
object GFG {
    // Method 1
    // To sort a string alphabetically
    fun sortString(inputString: String): String {
        // Converting input string to character array
        val tempArray = inputString.toCharArray()

        // Sorting temp array using
        Arrays.sort(tempArray)

        // Returning new sorted string
        return String(tempArray)
    }

    // Method 2
    // Main driver method
    @JvmStatic
    fun main(args: Array<String>) {
        // Custom string as input
        val inputString = "geeksforgeeks"
        val outputString = sortString(inputString)

        // Print and display commands

        // Input string
        println("Input String : $inputString")
        // Output string
        println("Output String : "
                + outputString)
    }
}
