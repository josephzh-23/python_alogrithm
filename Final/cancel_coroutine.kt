package Final

import kotlinx.coroutines.async
import kotlinx.coroutines.delay
import kotlinx.coroutines.isActive
import kotlinx.coroutines.runBlocking
internal object FooKt22 {
    @JvmStatic
    fun main(args: Array<String>) = runBlocking {

        var job = async {
            var i = 0
            // Using this isActive
            while (i != 100 && isActive) {
                i++
            }
            delay(300)
        }
        delay(100)
        job.cancel()
        println("canceled $isActive")
    }
}