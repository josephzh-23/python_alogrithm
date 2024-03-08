package Coding_Challenges

/*
answer: T = O(m*n)
S = O(m*n)
bottom up dp approach would be used here
 */


var memo = HashMap<Pair<Int, Int>, Int>()
var numTargets = 0
var numWords = 0
var ans = 0
var target = ""

/*
A char
a b c d
a b c d
 count will store char, and # of times it appears at a certain
 index for all a word
 */
var count = arrayOf(HashMap<Char, Int>())
/*
targetIdx: the idx from target we are picking
before the target idx everythign has been matched
for this target string

wordIdx: tells us from which idx in our words
are the valid string we can pick

The bf approach:
if find a match
1. Then accumulate, with dp (targetIdx + 1, wordIdx + 1), this is bad
this will loop thru all the words, resulting in TLE

2. So better solution       if we are looking for e
	a b e  d
	a b e  f        obviously if doing the for
	a b e  f
	a b e  f
so down here it means 4 ways to pick letter to match current . So
to opitmize you can do 4 * [dp() for each 1 word], and this would
 remove the
for loop for down below where we do

- this is where we used the count with dictionary
The count will store at each index,
the count of the letters there
 */
fun numOfWaysFormTargetString(words: Array<String>, target: String): Double {


    // Usi
    var mod = Math.pow(10.0, 9.0) + 7
    numTargets = target.length
    numWords = words[0].length

    for (i in 0 until numWords) {
        words.forEach { w ->
            // grab 1st let
            var c = w[i]

            //preprocessing for the counts
            count[i][c] = count[i][c]!! + 1
        }
    }
    return dp(0, 0)%mod

}

fun dp(targetIdx: Int, wordIdx: Int): Int {

    if (memo.contains(Pair(targetIdx, wordIdx))) {
        return memo[Pair(targetIdx, wordIdx)]!!
    }

    // This means if we have found the targets for 1 string then return
    // 1
    if (targetIdx == numTargets) {
        return 1

       // this means if we have reached end of idx, and found no match

    } else if (wordIdx == numWords) {
        return 0
    }
    ans = 0

    // the character to match
    var c = target[targetIdx]

    // skip cur wordIdx which is better way
    // instead of for i in range(wordIdx, numSwords)
    /*
    if wordIdx = 4, we should skip wIdx 1, 2, 3
    using for loop is not good for this, so we use
    wordIdx below

    so here we decide to skip the current word idx
     */
    ans = dp(targetIdx, wordIdx + 1)

    // try to use current word index
    // Check the explanation above if there is a match
    // there are potentnail matches

    // Same as the one from before
    if (count[wordIdx].contains(c)) {
        ans += dp(targetIdx + 1, wordIdx + 1) *
                count[wordIdx][c]!!
    }
    memo[Pair(targetIdx, wordIdx)] = ans
    return ans
}
