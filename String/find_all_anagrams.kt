package String

import java.util.*

/*
OC : O (alphabet letter size * len(s))

construct sth like this
String :
a b c d e b a c b
shash :   idx:0  1 2  3 4    each idx represent   -> 'a' 'b' 'c' 'd' 'e'
       count: 1  1 1  1 1

phash :   idx: 0 1 2  3 4
       count: 1  1 1  1 1

Notice this can also be done using dictionary here
 */
fun findAnagrams(s:String, p:String): List<Int>{
    var ans = mutableListOf<Int>()
    var shash = IntArray(26)
    var phash = IntArray(26)

    var (left ,right) = Pair(0, 0)
    var pLen = p.length
    var sLen = s.length
    if(s.length==0 || s==null) return ans

    // store at each idx the frequencey of that letter
    var count = IntArray(26)

    if(sLen < pLen){

        return ans
    }


    // this is for the first window only with windowLen = 3
    // s: abc   p: abc
    // set up all the counts
    while(right < pLen){
        phash[p[right]-'a']++
        shash[s[right++]-'a']++
    }
    // So start at the right index
    right-=1
    // N


    // THe key butter here
    /*
    and with each iteration
    1. dec count for leftMost char, inc left pt
    2. inc count for rightmost char, int right pt
    2. If phash size == shash, add the left index to resList
     */
    while(right <sLen){

        // This is when all hash.size are the same
        // then add the left pointer idx
        if(Arrays.equals(phash, shash)){
            ans.add(left)
        }

        right++
        // Increase the counter for the character at the right
        if(right!= sLen){
            shash[s[right]-'a']++
        }

        // decrease counter for elem atht left
        shash[s[left]-'a'] --
        left++
    }
    ans.forEach{
        println(it)
    }
    return ans
}


fun main(){

    var s = "abab"
    var p = "ab"


    findAnagrams(s, p)

}