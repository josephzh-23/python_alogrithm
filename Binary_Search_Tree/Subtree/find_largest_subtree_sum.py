'''
    1
   / \
  -2  3
 / \
4   5

Check at 1 left subtree sum = 7 and right subtree sum = 3
So that's why they r different here

Do a preorder traversal : l , root, r to start here
'''
def findLargestSubtreeSumUtil(r, ans):
    if not r:
        return 0

    leftsum = findLargestSubtreeSumUtil(r.l, ans)
    rightsum = findLargestSubtreeSumUtil(r.r, ans)

    cursum = r.data + leftsum + rightsum
    ans = max(ans, cursum)

    return ans


def findLargestSubtreeSum(r):
    if not r: return 0

    ans = float('-inf')
    findLargestSubtreeSumUtil(r, ans)
    return ans












