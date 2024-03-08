package top_tricks


// THis will change the character in the string at each position and then
// print sth in the end
fun main() {
    var word = "a"
    for (j in 0 until word.length) {
        var k = 'a'.code
        val arr = word.toCharArray()
        while (k <= 'z'.code) {
            arr[j] = k.toChar()


            val str = StringBuilder().append(arr).toString()
            println(str)
            k++
        }
    }
}