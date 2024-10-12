from typing import List

from Binary_tree.BSTNode import TreeNode


def helper(arr, left, right):
    if (right < left or left >= right):
        return None
    # get the binary middle point each time and then do a division here or there

    mid = left + (right -left) //2

    node = TreeNode(arr[mid])

    node.l = helper(arr, left, mid - 1)
    node.r = helper(arr, mid + 1, right)

    return node

def sortedArrayToBST(nums:List[int]) -> TreeNode:
    if not nums:
        return None

    ans = helper(nums, 0, len(nums))
    print("the answer is", ans)
    return ans

