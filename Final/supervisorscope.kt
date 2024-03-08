package Final

import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking

// This ensures when child fails parent will then be ok here

fun main() {

    kotlinx.coroutines.GlobalScope.launch{
        println("joseph")
    }
}