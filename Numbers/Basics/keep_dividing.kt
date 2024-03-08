package Numbers.Basics

// This allows you to keep dividing here
fun main() {
    intToRoman(115)
}
fun intToRoman(num: Int): String {
    var num = num
    while(num > 0){

        num /= 10
        println(num)
        // so you will then get 15, 1 and so forth here
    }
    return " "
}