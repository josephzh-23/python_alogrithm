'''

Want to find the biggest binary tree value here


TreeNode constructMaximumBinaryTree([3,2,1,6,0,5]) {
    // 找到数组中的最大值
    TreeNode root = new TreeNode(6);
    // 递归调用构造左右子树
    root.left = constructMaximumBinaryTree([3,2,1]);
    root.right = constructMaximumBinaryTree([0,5]);
    return root;
}

'''
import sys
from typing import List

from Binary_tree.BSTNode import TreeNode


def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    return build(nums, 0, len(nums) - 1)


# 定义：将 nums[lo..hi] 构造成符合条件的树，返回根节点
def build(nums: List[int], lo: int, hi: int) -> TreeNode:
    # base case
    if lo > hi:
        return None

    # 找到数组中的最大值和对应的索引
    index, maxVal = -1, -sys.maxsize
    for i in range(lo, hi + 1):
        if maxVal < nums[i]:
            index = i
            maxVal = nums[i]

    # 先构造出根节点
    root = TreeNode(maxVal)
    # 递归调用构造左右子树
    root.l = build(nums, lo, index - 1)
    root.r = build(nums, index + 1, hi)

    return root

# and then the above is what happens here and there is no easy way out
constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])











    # find the max value here then the root here
    # and then get the max val on the left and the right
