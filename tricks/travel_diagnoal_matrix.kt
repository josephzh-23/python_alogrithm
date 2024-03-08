package tricks

// Travel diagnol in matrix leetcode
// downward over here


// For the specicic problem see nth queen
fun main() {
    var g = arrayOf(intArrayOf(0, 0, 0),
            intArrayOf(0, 0, 0),
            intArrayOf(0, 0 ,0))
    travelDiagnol(g)
}
// basically make it 1 and that's the start
fun travelDiagnol(g: Array<IntArray>){
    var (i, j)=Pair( 0, 0)
    while(i < g.size && j < g[0].size){
        g[i][j] =1
        i++
        j++
    }
    println(g)
}