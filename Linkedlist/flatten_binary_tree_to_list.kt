class Node(var data: Int) {
    var left: Node? = null
    var right: Node? = null
}

// Check the notes here and then you can see what's going on

object Solution2 {
    var prev: Node? = null
    fun flatten(root: Node?) {
        if (root == null) return
        flatten(root.right)
        flatten(root.left)

        // Set the right of the current to previous
        root.right = prev
        // set left to null
        root.left = null
        prev = root
    }

    @JvmStatic
    fun main(args: Array<String>) {
        var root: Node? = Node(1)
        root!!.left = Node(2)
        root.left!!.left = Node(3)
        root.left!!.right = Node(4)
        root.right = Node(5)
        root.right!!.right = Node(6)
        root.right!!.right!!.left = Node(7)
        flatten(root)
        while (root!!.right != null) {
            print(root.data.toString() + "->")
            root = root.right
        }
        print(root.data)
    }
}