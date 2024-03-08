package Dynamic_programming

fun fib(N: Int): Int {
    if (N <= 1) {
        return N
    }
    val cache = IntArray(N + 1)
    cache[1] = 1
    for (i in 2..N) {
        cache[i] = cache[i - 1] + cache[i - 2]
    }
    return cache[N]
}

fun main(args: Array<String>) {
    val n = 9
    println(fib(n))
}