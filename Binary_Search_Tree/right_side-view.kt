package Tree

import Tree.Basic.TreeNode
import java.util.*



    fun main(){
        var root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        rightSideView(root)
    }
// And then using this we

    // start with printing the first of each level
    fun rightSideView(root: TreeNode?): MutableList<Int?>? {

        if(root==null){
            return null
        }
        // start with a queue
        val q = LinkedList<TreeNode>()

        q.add(root)
        while(!q.isEmpty()){
            var sizeOfCurLevel = q.size

            for(i in 0 until sizeOfCurLevel){
                var node = q.pop()
                print(node.value)
                var j = 0
                if(j==0){
                    node.left?.run{
                        q.add(this)
                    }
                    node.right?.run{
                        q.add(this)
                    }
                }
            }
        }
        return null
    }