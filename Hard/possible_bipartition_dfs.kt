import java.util.*

fun main() {


}

fun isBiparitie(g: Array<IntArray>) : Boolean {

    var colors = IntArray(g.size)
    Arrays.fill(colors, 0)

    // Fill this with 0 here

    for (i in 0 until g.size) {
        if (colors[i] == 0 && !validColor(g, colors, 1, i))
            return false
    }
    return true
}

fun validColor(g: Array<IntArray>, colors: IntArray, color: Int, node: Int): Boolean {
    // Step 1: set the color

    // If color already set then check to see if it's 0 or not
    if (colors[node] != 0) {
        return colors[node] == color;
    }
    for (neigh in g.get(node)) {
        // Will pass in the opposite here
        if (!validColor(g, colors, -color, neigh)) {
            return false
        }
    }
    return true

}