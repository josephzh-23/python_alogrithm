package String_manipulation


//Create RemoveDuplicatesExample4 class to remove duplicates from the string
internal object RemoveDuplicatesExample4 {


    // Create removeDuplicates() method to remove duplicates using indexOf() method
    fun removeDuplicates(str: String) {
        //Create an empty string
        var newstr = String()

        //calculate length of the original string
        val length = str.length

        // Traverse the string and check for the repeated characters
        for (i in 0 until length) {
            // store the character available at ith index in the string
            val charAtPosition = str[i]

            // check the index of the charAtPosition. If the indexOf() method returns true add it to the resuting string
            if (newstr.indexOf(charAtPosition) < 0) {
                newstr += charAtPosition
            }
        }
        //Print string after removing duplicate characters
        println(newstr)
    }

    // Backtracking.Tree.Hard.Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main() method start
    @JvmStatic
    fun main(args: Array<String>) {
        // Create a string variable with default value
        val str = "JavaTpoint is the best learning website"
        //call removeDuplicates() method for removing duplicate characters
        removeDuplicates(str)
    }
}