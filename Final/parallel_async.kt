package Final

import kotlinx.coroutines.*
import kotlin.system.measureTimeMillis

fun main() = runBlocking {


    val executionTime = measureTimeMillis {

        val result1: Deferred<String> = async {
            println("debug: launching job1: ${Thread.currentThread().name}")
            delay(500)
            return@async "dd"
        }


        val result2: Deferred<String> = async {
            println("debug: launching job2: ${Thread.currentThread().name}")
            delay(3000)
            return@async "dsfsd"
        }

//                setTextOnMainThread("Got ${result1.await()}")
//                setTextOnMainThread("Got ${result2.await()}")
        // can do sth about the result above here
        println("Got ${result1.await()}")
        println("Got ${result2.await()}")
    }
    println("debug: job1 and job2 are complete. It took ${executionTime} ms")
}
