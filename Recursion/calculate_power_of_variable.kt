package January_3rd

object Main {
    @JvmStatic
    fun main(args: Array<String>) {
        val base = 5
        val x = 3
        println("Required Power is " + power(base, x))
    }

    //Recursive Function
    fun power(base: Int, x: Int): Int {
        return if (x == 0) 1 else base * power(base, x - 1)
    }
}