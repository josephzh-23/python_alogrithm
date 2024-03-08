package Util

fun main(){


    val lambda : (String, String) -> String = { first: String, last: String ->
        "My name is $first $last"
    }

    val square:(Int) -> Int = {number->
        number *number
    }
    println(square(5))

    val printName: (String) -> Unit = {
        println(it)
    }
    printName("joseph")
}
