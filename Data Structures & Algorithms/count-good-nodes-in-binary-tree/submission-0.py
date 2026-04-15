# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def good(root: TreeNode, maxVal: int) -> None:
            if root.val >= maxVal:
                self.res += 1
                maxVal = root.val
            if root.left:
                good(root.left, maxVal)
            if root.right:
                good(root.right, maxVal)
        good(root, -101)
        return self.res