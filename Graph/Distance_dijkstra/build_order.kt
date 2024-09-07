package Graph.Top_6

import January_3rd.print
/*
You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
 */


/*
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
 */

/*

Course list problem
 */

// This is the brute force solution
fun isPossible(V: Int, prerequisites: Array<CharArray>) : Array<Project?>? {
    // This will be used for iteration later on
    val projects = arrayListOf<Project>()

    // This needs to be the name as said
    val set = mutableSetOf<Char>()
    val m = prerequisites.size
    for (i in 0 until m) {
        val start = prerequisites[i][0]
        val end = prerequisites[i][1]


        val startNode = Project(start)
        val endNode = Project(end)
        startNode.addNeighbor(endNode)
        if (!set.contains(startNode.name)) {
            set.add(startNode.name)
            projects.add(startNode)
        }

        if (!set.contains(endNode.name)) {
            set.add(endNode.name)
            projects.add(endNode)
        }
    }


    val orders = arrayOfNulls<Project>(projects.size)
    // This will be end of list
    var endOfList = addNonDependent(orders, projects, 0)

    // Add nondepdendant, insert porjects with 0 depdencies into the
    // order array

    var toBeProcessed = 0
    while(toBeProcessed < projects.size){
        val cur = orders[toBeProcessed]

        if(cur == null) return null // Circular dependency the end is found now

        val children = cur.children
        for(child in children){
            child.numberDependencies--
        }

        // Add children that have no dependencies here
        endOfList = addNonDependent(orders, children, endOfList )
        toBeProcessed++

    }
    return orders

}


object tUf {
    @JvmStatic
    fun main(args: Array<String>) {
        val N = 4
        val prerequisites = Array(5) { CharArray(2) }
        prerequisites[0][0] = 'a'
        prerequisites[0][1] = 'd'
        prerequisites[1][0] = 'f'
        prerequisites[1][1] = 'b'
        prerequisites[2][0] = 'b'
        prerequisites[2][1] = 'd'
        prerequisites[3][0] = 'f'
        prerequisites[3][1] = 'a'
        prerequisites[4][0] = 'd'
        prerequisites[4][1] = 'c'
        isPossible(N, prerequisites).print()
//        if (ans) println("YES") else println("NO")
    }
}


/* insert Projects w/ 0 dependencies into the order array */
fun addNonDependent(inDegree: Array<Project?>, Projects: ArrayList<Project>, offset: Int): Int {
    var offset = offset
    for (Project in Projects)
        if (Project.numberDependencies == 0)
            inDegree[offset] = Project
            ++offset
    return offset
}
/*
*
* 2. Initialize a buildOrder array. Once we determine a Project's build order, we add it to the array.
* We also continue to iterate through the array, using a toBeProcessed pointer to
* point to the next node to be fully processed.
*
* 3. Find all the nodes with 0 incoming edges and add them to a buildOrder array.
* Set a toBeProcessed pointer to the beginning of the array.
*
* Repeat until toBeProcessed is at the end of the buildOrder
*
* 1. Read node toBeProcessed.
*  >> If node == null, then all remaining nodes have a dependency and we have detected a cycle
* 2. For each child of node:
*  >> decrement child.dependencies (# of incoming edges)
*  >> if child.dependencies is 0, add child to end of buildOrder
        ###

 */