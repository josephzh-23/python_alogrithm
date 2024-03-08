package Tree.Array

import Tree.Basic.TreeNode
import java.util.*


/*
Do a preorder:
left subtree -> right subtree here
->
0. Build a root node
1. Encode into a string first with comma and then
2. Split into left and right tree

3. If both children null then go up


Deserializing: use another one here
When the value is character "n" we know it's null here
 */

fun serialize(r: TreeNode?, str: String): String { // recursive serialization here
    var str = str
    if (r == null) {
        str += "null"
    } else {
        str += (r.value).toString() + ","
        str += serialize(r.left, str)
        str += serialize(r.right, str)
    }
    return str
}

// Deserialize here based on the data
class Codec {
    fun rdeserialize(l: MutableList<String>): TreeNode? { // Recursive deserialization.
        if (l[0] == "null") {
            l.removeAt(0)
            return null
        }

        val root = TreeNode(Integer.valueOf(l[0]))
        // We remove the first value of each node here so you can process the next one
        l.removeAt(0)
        root.left = rdeserialize(l)
        root.right = rdeserialize(l)
        return root
    }

    // Decodes your encoded data to tree.
    fun deserialize(data: String): TreeNode? {
        val data_array = data.split(",".toRegex()).dropLastWhile { it.isEmpty() }.toTypedArray()
        val data_list: List<String> = LinkedList<String>(Arrays.asList(*data_array))
        return rdeserialize(data_list.toMutableList())
    }
}






