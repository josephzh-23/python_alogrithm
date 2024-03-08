package tricks

fun main() {
    var g = arrayOf(intArrayOf(0, 0, 0),
            intArrayOf(0, 0, 0),
            intArrayOf(0, 0 ,0))
    traverseTheColumnRow(g)
}
/*
        1
     1  1   1
        1
 */
// This traverse the row and the column of that cell
// belongs to like a cross
fun traverseTheColumnRow(g: Array<IntArray>){
    var column = 1
    var row = 1
    var n = g.size

    // And if the column.size == row
    for(i in 0 until n){

        // Change everything for that column
        g[i][column] = 1
        // change for the row
        g[row][i] =1
    }
    println(g.toString())
}
