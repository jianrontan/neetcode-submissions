# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def maxChild(root):
            if not root:
                return 0
            leftMax = max(maxChild(root.left), 0)
            rightMax = max(maxChild(root.right), 0)
            self.res = max(leftMax + rightMax + root.val, self.res)
            return root.val + max(leftMax, rightMax)
        maxChild(root)
        return self.res