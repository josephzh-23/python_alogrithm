package top_tricks


fun main() {
    var str = swapNumber("joseph", 0, 2)
    println(str)
}
// Using this can be very helpful
fun swapNumber(str:String, i: Int, j: Int): String{
    var cArray = str.toCharArray()

    // Swap the first one
    var temp = cArray[i]
    cArray[i] = cArray[j]
    cArray[j] = temp
    return StringBuilder().append(cArray).toString()

}

// Here we basically swap the number here

