package Hard

fun reachingPointsBetter(sx: Int, sy: Int, tx: Int, ty: Int): Boolean {
    var tx = tx
    var ty = ty
    while (tx >= sx && ty >= sy) {
        if (sx == tx && sy == ty) return true
        if (tx > ty) tx -= ty else ty -= tx
    }
    return false
}