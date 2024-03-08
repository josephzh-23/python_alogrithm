package tricks

import java.util.*


fun main(args: Array<String>) {
    val arr: Array<String> //declaring array
    arr = arrayOf("joseph", "jose", "ee")
//    Arrays.sort(arr) { a: String, b: String -> Integer.compare(a.length, b.length) }

     Arrays.sort(arr)
    arr.forEach{
        println(it)
    }
}
