import org.apache.poi.xwpf.usermodel.XWPFDocument
import java.io.IOException
import java.nio.file.Files
import java.nio.file.Paths
import java.util.*


object ReadParseDocument2 {
    @JvmStatic
    fun main(args: Array<String>) {

        var wordList = listOf("why", "how", "what", "what's", "data type")
//        val fileName = "/Users/josephzh/Desktop/photo_app.docx"
        val fileName = "/Users/josephzh/Desktop/System_design.docx"
        XWPFDocument(
                Files.newInputStream(Paths.get(fileName))).use { doc ->

            // output the same as 8.1
            val list = doc.paragraphs
            for (paragraph in list) {
//                println(paragraph.text)
                for(word in wordList) {
//                    println(paragraph)
                    if(paragraph.text.startsWith(word, ignoreCase = true)) {
                        println(paragraph.text)
                    }
                }
            }
        }
    }
}