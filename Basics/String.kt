package Util


fun main() {
    // Using the string function
    var name = "joseph"
    var c = name

    // Substring
    var new = name.substring(0, 2).also{
        println(it)
    }
}