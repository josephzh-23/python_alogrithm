package Util

// This will print dictionary of any kind

fun printDictionary(dict: HashMap<*, *>){

    dict.entries.forEach{

        println("${it.key}, ${it.value}")
    }
}