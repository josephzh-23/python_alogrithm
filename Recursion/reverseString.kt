package January_3rd

internal class StringReverse {
    /* Function to print reverse of the passed string */
    fun reverse(str: String?) {
        if (str == null || str.length <= 1) println(str) else {
            print(str[str.length - 1])
            reverse(str.substring(0, str.length - 1))
        }
    }

    companion object {
        /* Driver program to test above function */
        @JvmStatic
        fun main(args: Array<String>) {
            val str = "Geeks for Geeks"
            val obj = StringReverse()
            obj.reverse(str)
        }
    }
}