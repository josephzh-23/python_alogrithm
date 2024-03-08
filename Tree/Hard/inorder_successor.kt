package Tree.Hard

import Tree.Basic.TreeNode

fun main() {

}

/*
A couple of scenarios here

So there are a couple of scenarios here
We want the in order successor here
- if it's 4 ->
    7
  4    10
2  6  8  12
  5
 2 types of Situations:
if it's p = 4, then the next greatest element = 5
if p = 12, then next greatest is 10 which is the parent

 */
fun inOrderSuccessor(root: TreeNode, p: TreeNode):TreeNode?{

    if(root == null){
        return null
    }
    var cur = root
    //keep track of the previous here
    var parent: TreeNode? = null

    while(cur!=null){
        // 12 > 7 we want to go left
        if(cur.value > p.value){
            parent = cur
            cur = cur.left!!

            // the smaller value 5 < 7 we want to go rigth
        }else{
            cur = cur.right!!
        }
    }
    return parent
}