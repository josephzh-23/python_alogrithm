package Final

import kotlinx.coroutines.*

internal object FooKt222 {
    @JvmStatic
    fun main(args: Array<String>): Unit = runBlocking {

        var job2 = launch {
            try {
                var job = launch {
                    try {
                        Integer.parseInt(null)
                        println("josep")
                    } catch (e: Exception) {

                        // Using this make sure the parent will catch the exception here
                        if (e is CancellationException) {
                            throw e
                        }
                        println("didn't work ")
                    }
                }
            } catch (e: Exception) {

                println("parent's exception")
            }

        }
        job2.invokeOnCompletion { throwable ->
            if (throwable != null) {
                println("Parent job failed: ${throwable}")
            } else {
                println("Parent job SUCCESS")
            }
        }
    }
}