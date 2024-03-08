package String


fun main() {


    var coo = null
    var res = coo as? String
    println(res)
}
// this way we go towards the middle from the back
// and the start
private fun isPalindrome(s: String, start: Int, end: Int): Boolean {
    var start = start
    var end = end
    while(start < end){
        if(s[start] != s[end]){
            return false
        }
        start++
        end--
    }
    return true
}
