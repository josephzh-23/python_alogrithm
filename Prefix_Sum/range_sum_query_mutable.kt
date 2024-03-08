package Prefix_Sum

/*
Done with the problem leetcode
Sum node

Segment tree could be implemented using either an array or a tree.
For an array implementation, if the element at index i
 is not a leaf,

 its left and right child are stored at index
 2i and 2i + 1 respectively here
 */


class NumArray(nums: IntArray) {

    // Start index and end index here
    inner class SegmentTreeNode(var start: Int, var end: Int) {
        var left: SegmentTreeNode? = null
        var right: SegmentTreeNode? = null
        var sum = 0
    }

    var root: SegmentTreeNode? = null

    init {
        root = buildTree(nums, 0, nums.size - 1)
    }

    /*
     TC : O(n) this is the preprocessing part
          Convert an sorted array into a bst here
          s
    If the element @ index i is not a leaf, its right and left child
    are stored at index 2i and 2i + 1 respectively

        -
     */
    private fun buildTree(nums: IntArray, start: Int, end: Int): SegmentTreeNode? {
        return if (start > end) {
            null
        } else {
            val ret = SegmentTreeNode(start, end)
            if (start == end) {
                ret.sum = nums[start] // leaf nodes
            } else {
                val mid = start + (end - start) / 2
                ret.left = buildTree(nums, start, mid)
                ret.right = buildTree(nums, mid + 1, end)
                ret.sum = ret.left!!.sum + ret.right!!.sum
            }
            ret
        }
    }

    // TC : O(logn)
    fun update(i: Int, `val`: Int) {
        updateHelper(root, i, `val`)
    }

    /*
When we update the array at some index i, need to rebuild the segment
tree, need to update parent nodes that contain sums of the modified
element here
- a bottom up approach here

     */
    fun updateHelper(root: SegmentTreeNode?, pos: Int, `val`: Int) {

        // found leaf node to be updated at the very bottom
        // Check the diagram here
        if (root!!.start == root.end) {
            root.sum = `val`
        } else {

            // Parent node here
            val mid = root.start + (root.end - root.start) / 2
            if (pos <= mid) {
                updateHelper(root.left, pos, `val`)
            } else {
                updateHelper(root.right, pos, `val`)
            }
            // Parent sum is updated after child is updated
            root.sum = root.left!!.sum + root.right!!.sum
        }
    }

    fun sumRange(i: Int, j: Int): Int {
        return sumRangeHelper(root, i, j)
    }

    // TC : O(logn)
    fun sumRangeHelper(root: SegmentTreeNode?, start: Int, end: Int): Int {
        // if you found out the node that matches your search return its value
        return if (root!!.start == start && root.end == end) {
            root.sum
        } else {
            val mid = root.start + (root.end - root.start) / 2 // overflow conditions
            if (end <= mid) {
                // move left
                sumRangeHelper(root.left, start, end)
            } else if (start >= mid + 1) {
                // move right
                sumRangeHelper(root.right, start, end)
            } else {
                // consider both nodes
                sumRangeHelper(root.left, start, mid) + sumRangeHelper(root.right, mid + 1, end)
            }
        }
    }
}


