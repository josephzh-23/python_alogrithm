package Tree

import Tree.Basic.TreeNode


// O(h) where h is a tree height
//s:o(h) to keep track of the call stack
fun searchTree(r: TreeNode?, value: Int):Boolean{
    if(r==null || r.value == value){

        return true
    }

   return if(value < r.value)searchTree(r.left, value) else{searchTree(r.right, value) }

}