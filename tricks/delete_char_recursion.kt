package tricks


// sort words based on length

fun main() {
    var words = arrayOf("abcd")
    longestStrChain(words)
}
fun longestStrChainl(words: Array<String>): Int {
    //Start from back
//    for (i in 4 downTo 0) {
    recl(StringBuilder("abcd"), 4)
//    }
    return 0
//    longestStrChain(words)
}

// whether a valid word
fun recl(str: StringBuilder, i: Int): Boolean {
    if(i ==-1){
        return false
    }
    println("$str and $i")
    if(i!=0) {
        recl(str.deleteCharAt(i - 1), i - 1)
    }
    return true
}