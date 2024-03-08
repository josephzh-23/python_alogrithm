package Final

import java.io.File

import java.io.IOException
import java.util.*


object ReadWords {
    @JvmStatic
    fun main(args: Array<String>) {
        val file = File("/Users/josephzh/Desktop/photo_app.docx")
        val input = Scanner(file)
        var count = 0
        while (input.hasNext()) {
            println("sdd")
            val word: String = input.next()
            println(word)
            count = count + 1
        }
        println("Word count: $count")
    }
}


