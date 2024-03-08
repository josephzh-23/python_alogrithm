package String.Basic

fun changeString(){

    var curr = "joe"
    for (i in curr.indices){
        var temp1 = StringBuilder(curr)
        var c = 'a'
            // for looping alphabetically here
        while(c <= 'z'){
            temp1.setCharAt(i, c)
            println(temp1)
            // WOuld increase from 'a' to 'b' as mentioned
            c++
        }
    }
}
fun main() {
    changeString()
}