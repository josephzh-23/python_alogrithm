package Util

fun main() {
    val myStr1 = "Hello"
    val myStr2 = "Hello"
    val myStr3 = "Another String"
    println(myStr1 == myStr2) // Returns true because they are equal

    println(myStr1 == myStr3) // false

    //Using the compare to method
    // used to compare lexicologically

    val myStr4 = "Hello"
    val myStr5 = "Hello"
    println(myStr4.compareTo(myStr5))


}