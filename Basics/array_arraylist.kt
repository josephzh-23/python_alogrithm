package Util

val l: Array<ArrayList<Int>> = Array(5) { ArrayList<Int>() }


// Simplified below
val l2 = Array<ArrayList<Int>>(5) { ArrayList<Int>() }
val l3 = Array<ArrayList<Int>>(5) { ArrayList() }

val l4 = Array(5) { ArrayList<Int>() }