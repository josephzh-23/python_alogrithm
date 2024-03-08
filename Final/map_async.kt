import kotlinx.coroutines.async
import kotlinx.coroutines.awaitAll
import kotlinx.coroutines.runBlocking

internal object FooKt {
    @JvmStatic
    fun main(args: Array<String>) = runBlocking {

        val versions = listOf(1, 2, 3, 4)
       var answers  = versions.map{version->
            async{
                // do sth based on each verision
                return@async  listOf(1, 2, 3, 4)
            }
        }.awaitAll()
        answers.forEach{
            println(it)
        }
    }
}