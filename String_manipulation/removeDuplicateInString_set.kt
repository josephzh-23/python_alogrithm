package String_manipulation


internal object GFG {
    fun removeDuplicate(str: CharArray, n: Int) {
        // Create a set using String characters
        // excluding '\0'
        val s: HashSet<Char> = LinkedHashSet(n - 1)
        // HashSet doesn't allow repetition of elements
        for (x in str) s.add(x)

        // Print content of the set
        for (x in s) print(x)
    }

    // Driver code
    @JvmStatic
    fun main(args: Array<String>) {
        val str = "geeksforgeeks".toCharArray()
        val n = str.size
        removeDuplicate(str, n)
    }
}