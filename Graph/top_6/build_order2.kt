package Graph.Top_6

import Util.printList
import tricks.arr


// It doesn't work for some reason
fun main() {
    var projects = arrayOf("a", "b", "c", "d", "e", "f")
    var dependencies = arrayOf(arrayOf("d", "a"),
        arrayOf("b","f"),
        arrayOf("d", "b"),
        arrayOf("a", "f"), arrayOf("c", "d"))
   print(findBuildOrder(projects, dependencies))
}

fun findBuildOrder(projects: Array<String>, dependencies: Array<Array<String>>): Array<Project3?>? {
    val graph = buildGraph(projects, dependencies)
    return orderProjects(graph.nodes)
}

fun buildGraph(projects: Array<String>, dependencies: Array<Array<String>>): Graph {
    val graph = Graph()
    for (project in projects) project?.let { graph.getOrCreateNode(it) }
    for (dependency in dependencies) graph.addEdge(dependency[0].orEmpty(), dependency[1].orEmpty())
    return graph
}

fun orderProjects(project3s: ArrayList<Project3>): Array<Project3?>? {
    val order = arrayOfNulls<Project3>(project3s.size)
    var endOfList = addNonDependent(order, project3s, 0)
    var toBeProcessed = 0
    while (toBeProcessed < order.size) {
        val current = order[toBeProcessed] ?: return null
        // circular dependency, no remaining projects w/ 0 dependencies
        val children = current.children // remove myself as dependency
        for (child in children) child!!.decrementDependencies()
        endOfList = addNonDependent(order, children, endOfList) // add children that have no one depending on them
        ++toBeProcessed
    }
    return order
}

/* insert projects w/ 0 dependencies into the order array */
fun addNonDependent(order: Array<Project3?>, project3s: ArrayList<Project3>, offset: Int): Int {
    var offset = offset
    for (project in project3s) if (project!!.numberDependencies == 0) order[offset] = project
    ++offset
    return offset
}

class Graph {
    val nodes = ArrayList<Project3>()

    // This makes sure it's a map of no duplicates
    private val map = HashMap<String, Project3?>()


    fun getOrCreateNode(name: String): Project3? {
        if (!map.containsKey(name)) {
            val node = Project3(name)
            nodes.add(node)
            map[name] = node
        }
        return map[name]
    }

    fun addEdge(startName: String, endName: String) {
        val start = getOrCreateNode(startName)
        val end = getOrCreateNode(endName)
        start!!.addNeighbor(end)
    }
}

class Project3(val name: String) {
    val children = ArrayList<Project3>()
    private val map = HashMap<String, Project3?>()
    var numberDependencies = 0
        private set

    fun addNeighbor(node: Project3?) {
        if (!map.containsKey(node!!.name)) {
            children.add(node)
            node.incrementDependencies()
        }
    }

    fun incrementDependencies() {
        ++numberDependencies
    }

    fun decrementDependencies() {
        --numberDependencies
    }
}