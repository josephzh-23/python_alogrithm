package tricks

// Find if 2 arrays intersect here
fun intersect(A: IntArray, B: IntArray): Boolean {
    var i = 0
    var j = 0
    while (i < A.size && j < B.size) {
        if (A[i] == B[j]) return true
        if (A[i] < B[j]) i++ else j++
    }
    return false
}