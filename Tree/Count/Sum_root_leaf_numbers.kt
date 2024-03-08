package Tree.Count

import Tree.Basic.TreeNode


fun main() {

}
fun sumRootLeafNumbers(r: TreeNode?, value: Int):Int{

    // We will try to add 10 each time we get to the end here

    //
    if (r == null) {
        return 0
    }

    // Update the value here with a number * 10
    var value = value * 10 + r.value

    // If current node is leaf, then return the current value of val
    if(r.left == null && r.right == null){
        return value
    }

    // return the sun of values for left and right subtree
    //
    return sumRootLeafNumbers(r.left, value) + sumRootLeafNumbers(r.right, value)

}
