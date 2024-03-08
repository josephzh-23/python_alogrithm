package Split

// Increase sth by 1 the frequency

// You are given the string here "aacaba"

// https://leetcode.com/problems/number-of-good-ways-to-split-a-string/description/
fun numSplits(s: String) {

    var goodSplits = 0 // Have a left dict and a right dict
    var left = IntArray(26)
    var right = IntArray(26)
    for (i in 0 until s.length) {
        var c = s[i] // Build the right one first
        right[c - 'a']++
    }

    // After the building above a would then become "aacaba" the entire
    // word here
    for (i in 0 until s.length) {
        var c = s[i]

        /*
        This would be
        "a"    "acaba"
        "aa"    "caba"
         */
        left[c - 'a']++
        right[c - 'a']--

        var distinctCharOnTheLeft = getDistinct(left)
        var distinctCharOnTheRight = getDistinct(right)

        if(distinctCharOnTheLeft == distinctCharOnTheRight){
            goodSplits++
        }
    }
    print(goodSplits)
}

fun getDistinct(counts: IntArray): Int{

    var totalDistinct = 0
    for(c in counts){

        if(c!=0){
            totalDistinct++
        }
    }
    return totalDistinct
}

