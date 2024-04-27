package min_max



// Find all the anargsms

//a: abcdefg
// b: abc

fun main() {
    val a = charArrayOf('a','b','c','d','e')
    val b = charArrayOf('a','b','c')
    findAllAnagrams(a, b).forEach{
        println(it)
    }
}
fun findAllAnagrams(a: CharArray, b: CharArray):MutableList<Int>{
    val res = mutableListOf<Int>()

    // To find the 2
    val amap  = HashMap<Char, Int>()
    val bmap  = HashMap<Char, Int>()


    // Start this for the smaller size which is b
    for(i in 0 until b.size){

        amap.apply {
            put(a[i],getOrDefault(a[i], 0) + 1)
        }
        bmap.apply {
            put(b[i],getOrDefault(b[i], 0) + 1)
        }
    }

    // A will be bigger array

    // THe magic trick here
    for(i in 0 until a.size - b.size){

        // Making sure they are anagrams here
        if(amap == bmap){
            res.add(i)
        }
        // remove the count of first char
        amap[a[i]] = amap[a[i]]!! -1

        // add 1 to the count of newly added character

        // Fix this in a little bit and also Sliding_window.practice string problems here
        amap[a[i]] = amap[a[i + b.size]]!! +1
    }

    if(amap == bmap){

        res.add(a.size -b.size)
    }

    return res
    // This is for the last iteration


    // And then

}

fun isAnagram(pArr: IntArray, sArr: IntArray): Boolean {
    for (i in pArr.indices) {
        if (pArr[i] != sArr[i]) {
            return false
        }
    }
    return true
}











