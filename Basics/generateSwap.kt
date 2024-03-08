package Basics

import swap

fun main() {

    val p = intArrayOf(3, 1, 2)
    // generate the swap here
    for(i in p.indices) {
        for(j in i+1 until p.size) {
            val ans = swap(p, i, j)
            println(ans.joinToString(""))

        }
//        if(i == p.size -1){
//            val ans2 = swap(p, i, 0)
//            println(ans2.joinToString(""))
//        }


        // we have to make ihis exclusive
    }
}