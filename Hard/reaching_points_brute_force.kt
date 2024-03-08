package Hard

//Find the
fun main() {

    reachingPoints(1, 1, 3, 5)
}

fun reachingPoints(sx: Int, sy: Int, tx: Int, ty: Int): Boolean {
    if (sx > tx || sy > ty) return false

    if (sx == tx && sy == ty) {
        return true
    }else {
        return reachingPoints(sx + sy, sy, tx, ty) || reachingPoints(sx, sx + sy, tx, ty)
    }
}