package Graph.Top_6


// This is the starting point you have a project with a list of proejcts

// We want the number of depencies associated with this why so important
class Project(val name: Char) {

    // This iwillb be important for iteration later on here
    val children = ArrayList<Project>()
    private val map = HashMap<Char, Project>()

    // Will be used to sort later on so no worries right now
    var numberDependencies = 0

    fun addNeighbor(node: Project) {
        if (!map.containsKey(node.name)) {
            children.add(node)
            numberDependencies++
        }
    }

}