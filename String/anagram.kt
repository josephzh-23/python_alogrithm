package String
// These 2 are anagrams then as said
// you rearrange letter ,and form another word basically
//Build this for string 1 and string 2
// loop thru string and then compare

// Anagram : "cinema"   "iceman"
const val MAX_CHAR = 256
fun areAnagram(s1: String, s2: String): Boolean {
    val counts = IntArray(MAX_CHAR) { 0 }
    print(counts)
// [10, 20, 30, 40, 50]
//    if(s1.length!= s2.length){
//        return false
//    }
    // This means for each letter in s1 inc by 1
    // for s2 do the same dec by 1
    for (i in s1.indices) {
        // The position s1[i].code should be same as s2[i].code
        // at any point in this
        counts[s1[i].code - 'a'.code] += 1
        counts[s2[i].code - 'a'.code] -= 1
    }

    for (i in 0 until MAX_CHAR) {
        if (counts[i] != 0) {
            return false
        }
    }
    // So if any non-zero value
    return true
}


fun main() {
    println(areAnagram("iceman", "cinema"))
}