import Tree.Basic.TreeNode
import java.lang.Integer.max


// https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
fun main() {


    val r = TreeNode(-10)
    r.left = TreeNode(9)
    r.right = TreeNode(20)
    r.right!!.left = TreeNode(15)
    r.right!!.right = TreeNode(7)
    var s = Sole()
    s.maxPathSum(r)
}

// This will be a post order traversal
class Sole{

    // This will hold the result as we traverse thru each path here
    var res = 0

    fun maxPathSum(root: TreeNode?): Int {
        maxPathSumUtil(root)
        return res
    }

    // This util return sum without the splitting
    fun maxPathSumUtil(root: TreeNode?): Int {

        if (root == null) {
            return 0
        }
        var leftMax = maxPathSumUtil(root.left)
        var rightMax = maxPathSumUtil(root.right)
        // to get rid of negative here
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)
//        println("${root.value} and $leftMax and $rightMax")
        // Compute max path sum with the split here

        // Split means you can take both left and right
        /*
            3
           / \
          4   5     split means: 3 + 4 + 5
         */
        res = max(res, root.value + leftMax + rightMax)

        // we will be returining without the split here remember
        var sumWithoutSplit =  root.value + max(leftMax, rightMax)
        println(sumWithoutSplit)
        return sumWithoutSplit

    }
}
