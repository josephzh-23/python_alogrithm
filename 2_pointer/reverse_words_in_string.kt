package Array.two_pointer


fun main() {
    var s = "joseph"
    reverseWords(s.toCharArray())
}
fun reverseWords(s: CharArray): Unit {

    var l = 0
    var r = s.size -1
    var temp = 'c'
    for(i in s.indices){
        while(l < r){
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l++
            r--
        }
    }
    println(s)

}