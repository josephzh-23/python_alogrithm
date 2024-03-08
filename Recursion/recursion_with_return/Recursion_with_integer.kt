package Recursion.recursion_with_return

// f(4) = f(3) + f(2)
internal object recursion_with_integer {
    fun fib(n: Int): Int {
        return if (n <= 1) n else fib(n - 1) + fib(n - 2)
    }

    @JvmStatic
    fun main(args: Array<String>) {
        val n = 9
        println(fib(n))
    }
}