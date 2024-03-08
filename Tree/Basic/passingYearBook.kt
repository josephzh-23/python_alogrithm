package Tree.Basic

import Util.printList

// Have to follow the yearbook at the start until handed baack to the interviewer
// Here and then

/*

The following is what you want
The final output: a list of n integers output : whose element at i-1
= the # of signatures that will be present in student's yearbook once they
get it back

leetcode problem here
// Basically the condition stops when arr[i-1] = i and then that's done
they are out
 */

fun main() {
    var arr = intArrayOf(3, 2, 4, 1)
    passYearbook(arr)
}
fun passYearbook(arr: IntArray){

    // visited indexex from prevoius cycles to skip the counting
    var visited = BooleanArray(arr.size){false}
    var signatures  = IntArray(arr.size){0}


    // Every index has a root index, who started the passing cycle of
    //
    var roots = IntArray(arr.size) {-1}




    for(i in arr.indices){

        // if student at i was already visited
        if(visited[i]) continue
        visited[i] = true

        var j= -1
        // increment the signatures for current student
        // before she receives her own yearbook

        var student = arr[i]
        while (j!=i){
            signatures[i] +=1

            // student will then sent current yearbook to student at next index
            j = student -1
            visited[j] = true

            // root of next index = current index here
            roots[j] = i

            // next student
            student = arr[j]
        }

        //
        // set signatures of yearbooks that were not yet explored
        // because they had a root
        for(i in signatures.indices){
            if(roots[i] > -1){
                signatures[i] = signatures[roots[i]]
            }
        }

        print(signatures)
    }
}



