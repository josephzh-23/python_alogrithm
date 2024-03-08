package tricks

// sort words based on length

fun main() {
    var words = arrayOf("abcd")
    longestStrChain(words)
}
fun longestStrChain(words: Array<String>): Int {
    //Start from back
//    for (i in 4 downTo 0) {
        rec(StringBuilder("abcd"), 3, "bda")
//    }
    return 0
//    longestStrChain(words)
}

// whether a valid word
fun rec(str: StringBuilder, i: Int, word:String): Boolean {
    if(i ==-1){
        return false
    }

    var temp = str
    var deleted = temp[i]
    if(temp.deleteCharAt(i).toString()==word){

        return true
    }
    println("$temp and $i and $deleted")
    if(i!=0) {
        rec(temp.insert(i, deleted) , i - 1, word)
    }
    return true
}