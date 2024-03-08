package Util

fun printList(list: List<*>) {
    list.forEach {
        println(it)
    }

}


fun printArray(list: IntArray) {
    list.forEach {
        println(it)
    }

}
fun printNestedList(list: List<List<*>>) {
    list.forEach {
        it.forEach {
            println(it)
        }
    }

}