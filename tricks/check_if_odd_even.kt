package tricks

import java.util.*

object EvenOdd {
    @JvmStatic
    fun main(args: Array<String>) {
        val reader = Scanner(System.`in`)
        print("Enter a number: ")
        val num: Int = reader.nextInt()
        if (num % 2 == 0) println("$num is even") else println("$num is odd")
    }
}