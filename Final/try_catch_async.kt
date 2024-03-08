package Final

import kotlinx.coroutines.*

// Scope handling coroutines for a particular layer of my app

// How to throw exception with coroutine here
fun main() = runBlocking<Unit> {

    // If child 1 fails here neither child 2 or 3 will be cancelled as a dresut
    val scope = CoroutineScope(SupervisorJob())
    scope.launch {
        // Child 1
    }

    val deferred = GlobalScope.async {
        println("3. Exception created via async coroutine")

        // Nothing is printed, relying on user to call await
        throw ArithmeticException()
    }

    try {

        // Calling await wili make this work 
        deferred.await()
        println("4. Unreachable, this statement is never executed")
    } catch (e: Exception) {
        println("5. Caught ${e.javaClass.simpleName}")
    }


    // Handling exceptio in coroutine here and then
    // you can wrap the .await() call inside a try /catch block here


}