package Coding_Challenges

import java.util.*
import kotlin.collections.HashMap

/*
https://leetcode.com/problems/reorganize-string/
TC: O(nlogn)

Use a max heap-> b/c most frequent item here
1. this would mean O (logn)
2. can replace sorting for us

start with the most freq char
Use a hashmap

a -> 3      b -> 2     c -> 2

each time we take off a, also then take off b, since this is the next most
freq elemetn
a: 3      a: 2      a: 1
b: 1 ->   b: 0  ->  b: 0
c: 1      c: 1      c: 0

Each time a letter is used, use a diff character
so use a previous to keep track of pointer

*/
// Any 2 adj not the same
fun reorganizeString(s: String): String {
        // Step 1: create a map with count and freq
    // build this part first
    val counts: MutableMap<Char, Int> = HashMap()

    for(char in s){
        // This can be simplifed using getOrDefault()
        counts.apply {
            put(char, getOrDefault(char, 0) + 1)
        }
    }
    // Build this based on how many times the character has occured
    val maxHeap: Queue<Char> = PriorityQueue { a: Char, b: Char ->
        counts.get(a)!!- counts.get(b)!!
    }
    // This will sort automatically
    // counts.keys at this point will be
    maxHeap.addAll(counts.keys)
    var results = StringBuilder()
    while(maxHeap!=null){
        // this is the most freq char
        var cur = maxHeap.poll()
        // next most frequent
        var next = maxHeap.poll()

        // Add these 2 first
        results.append(cur)
        results.append(next)

        // update the count
        counts.put(cur, counts.get(cur)!! - 1)
        counts.put(next, counts.get(next)!! - 1)

        // Once they are popped
        // Check if any more current element and next element left
        if(counts.get(cur)!! > 0){
            maxHeap.add(cur)
        }
        if(counts.get(next)!! >0){
            maxHeap.add(next)
        }

        // If there is 1 character left and basically
        // nothing left to split it, then we just have to return
        // an empty string as expected in this example before
        // return the empty string here
        if(!maxHeap.isEmpty()){
            var last = maxHeap.remove()
            // once removed
            if(counts.get(last)!! > 1){

                return ""
            }
            results.append(last)
        }
        return results.toString()
    }

    var cur = maxHeap.remove()
    var next = maxHeap.remove()
    return "joseph"
}

fun main() {

//    reorganizeString("jooooseph")
}


fun reorganizeString3(s:String){
// build this part first
    val counts: MutableMap<Char, Int> = HashMap()

    for(char in s){
        // This can be simplifed using getOrDefault()
        counts.apply {
            put(char, getOrDefault(char, 0) + 1)
        }
    }
    // Based on the number of times this has happened

    val maxHeap: Queue<Char> = PriorityQueue { a: Char, b: Char ->
        counts.get(a)!!- counts.get(b)!!
    }

    maxHeap.addAll(counts.keys)

    var result = StringBuilder()
    while(!maxHeap.isEmpty()){
        
        val res =maxHeap.poll()

    }
}