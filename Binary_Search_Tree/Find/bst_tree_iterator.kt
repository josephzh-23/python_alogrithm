package Tree

import Tree.Basic.TreeNode

// There is also an easier time to do this
class BSTTreeIterator(var treeNode: TreeNode){
    var index = 0

    var list = mutableListOf<Int>()
    init{

    }
    fun inOrder(root: TreeNode?){
        if(root == null){
            return
        }
        inOrder(root.left)
        list.add(root.value)
        inOrder(root.left)

    }

    fun hasNext():Boolean {
        return index < list.size
    }
}
