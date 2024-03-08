package Final


import kotlinx.coroutines.*
import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.Dispatchers.Main
import kotlin.system.measureTimeMillis

fun main() = runBlocking {

    withContext(IO) {
        // Will wait and block both results here
        val executionTime = measureTimeMillis {

            // Async/Await returning a value
            // THIs allows you to return a value here
            // this allows you to return a value here
            val result1 = async {
                println("debug: launching job1: ${Thread.currentThread().name}")
               delay(2000)
                return@async "joseph"
            }.await()




            val result2 = async {
                println("debug: launching job2: ${Thread.currentThread().name}")
                delay(3000)
                return@async "joseph"

            }.await()
            println("Got result2: $result1")
            println("Got result2: $result2")

        }
        println("debug: job1 and job2 are complete. It took ${executionTime} ms")
//        superVisorJob()
    }



}



val handler = CoroutineExceptionHandler { _, exception ->
    println("Exception thrown in one of the children: $exception")
}

val childExceptionHandler = CoroutineExceptionHandler { _, exception ->
    println("Exception thrown in one of the children: $exception.")
}
fun getResultWithException(number: Int) {
    if (number == 2) {

        // tihs will cause a crash if not handled correctly as said
        throw Exception("Error getting result for number: ${number}") // treated like "cancel()"
        // and then using teh code over here we
    }
}


// Using this we can basically handle the exception inside the job that
// fails and that's it
//fun superVisorJob() {
//    val parentJob = launch {
//
//        supervisorScope { // *** Make sure to handle errors in children ***
//
//            // --------- JOB A ---------
//            val jobA = launch {
//                val resultA = getResultWithException(1)
//                println("resultA: ${resultA}")
//            }
//
//            // This allows you to handle the exception inside the child as said
//            // before right..
//            // --------- JOB B ---------
//            val jobB = launch(childExceptionHandler) {
//                val resultB = getResultWithException(2)
//                println("resultB: ${resultB}")
//            }
//
//            // --------- JOB C ---------
//            val jobC = launch {
//                val resultC = getResultWithException(3)
//                println("resultC: ${resultC}")
//            }
//        }
//    }
//
//    parentJob.invokeOnCompletion { throwable ->
//        if (throwable != null) {
//            println("Parent job failed: ${throwable}")
//        } else {
//            println("Parent job SUCCESS")
//        }
//    }
//
//}