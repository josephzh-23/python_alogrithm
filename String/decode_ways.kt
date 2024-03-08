package String


/*
THis is like the memoization solutino with the othere here
TC : O(n)
Space: O(n) here


A map can map to the following here

if you have the code
S = "226"   226 -> could be "BZ", "VF" or "BBF"
 */

// Using this TC: O(2^n) and that will not unchange here
// And then that's good here
class Solution15 {

    var result = 0

    fun find(s: String) {
        if (s.startsWith("0")) return

        // Here
        if (s.length <= 1) {
            result++
            return
        }

        // In the multiple cases here
        for(i in 0 until Math.min(2, s.length)){
            val value = Integer.parseInt(s.substring(0, i + 1))

            // This is right in between here
            // So if we have like 22 then we take this route here
            if(value in 1..26){
                find(s.substring(i + 1))
            }
        }
    }
}