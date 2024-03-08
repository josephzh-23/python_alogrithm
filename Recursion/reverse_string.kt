package Recursion

internal object GFG {
    /* Function to print reverse of the passed string */
    /*
    a: is the string that's passed in as said,
    n: size of the array
     */
    fun reverse(str: CharArray, index: Int, n: Int) {
        if (index == n) // return if we reached at last index or at the end of the string
        {
            return
        }
        // str[0]   1
        //
        val temp = str[index] // storing each character starting from index 0 in function call stack;
        reverse(str, index + 1, n) // calling recursive function by increasing index everytime
        print(temp) // printing each stored character while recurring back
    }

    @JvmStatic
    fun main(args: Array<String>) {
        val a = "Geeks for Geeks".toCharArray()
        val n = a.size
        reverse(a, 0, n)
    }
}
