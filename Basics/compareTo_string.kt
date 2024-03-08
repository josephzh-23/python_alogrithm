package Util

// Compare to function is used to compare string lexicologically
fun main() {
    var name1 = "joseph"
    var name2 = "zhou"
    // this < 0 because name 1 should come before name2
    println(name1.compareTo(name2))

    // this > 0 because name 2 comes before 1
    println(name2.compareTo(name1))

    // should be 0 here
    println(name2.compareTo(name2))
}