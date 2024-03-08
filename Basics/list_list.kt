package Basics

val listOfList = MutableList(3) { mutableListOf<Int>() }
// The following is better since no size initialized here
val resultList: MutableList<List<Int>> = ArrayList()
