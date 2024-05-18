package min_max

import java.lang.Integer.max

// O: O (2n) = O (n) visited twice
// O (min(m, n))
/*
The native approach is not good using dictionary
kind of slow
Use a set
2. If haven't seen add to set, inc right pter
3. If seen, rmv char using remove and inc left pter

O
 */

fun lengthOfLongestSubString(s:String):Int{

    var l = 0
    var r= 0
    var max = 0
    var hSet = HashSet<Char>()
    while(r< s.length){

        if(!hSet.contains(s[r])){
            hSet.add(s[r])
            r++
            max = max(hSet.size, max)
        }else{
            hSet.remove(s[l])
            l++
        }

    }
    return max
}


