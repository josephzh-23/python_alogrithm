package tricks

fun main() {

    var num = 123
    var numChars = num.toString().toCharArray()
    var dict = HashMap<Char, Int>()

    for(num in numChars){
        dict.put(num, dict.getOrDefault(num, 0)+1)
    }
    dict.forEach{
        println(it)
    }
}