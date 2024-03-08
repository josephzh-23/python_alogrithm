package String



fun reverseWords(s: CharArray): Unit {

    var l = 0
    var r = s.size -1
    var temp = 'c'
    for(i in s.indices){
        while(l < r){
            temp = s[l]
            s[r] = s[l]
            s[l] = temp
        }
    }

}