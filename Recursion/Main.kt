package January_3rd

fun main(args: Array<String>) {

    var sx = 1; var sy = 1
    var tx = 3; var ty= 5
    println("Hello World!")

    // Try adding program arguments via Run/Debug configuration.
    // Learn more about running applications: https://www.jetbrains.com/help/idea/running-applications.html.

    reachingPoints(1, 1, 3, 5).print()
}

fun reachingPoints(sx: Int, sy: Int, tx: Int, ty: Int): Boolean {
    if (sx > tx || sy > ty) return false
    return if (sx == tx && sy == ty) true else reachingPoints(sx + sy, sy, tx, ty) || reachingPoints(
        sx,
        sx + sy,
        tx,
        ty
    )
}

