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
            if not root.left and not root.right:
                self.res = max(root.val, self.res)
                return root.val
            leftMax, rightMax = 0, 0
            if root.left:
                leftMax = max(maxChild(root.left), 0)
            if root.right:
                rightMax = max(maxChild(root.right), 0)
            print(" ")
            print("node:", root.val)
            print("res:", self.res)
            print("leftMax:", leftMax)
            print("rightMax:", rightMax)
            print("node max path:", leftMax + rightMax + root.val)
            if leftMax + rightMax + root.val > self.res:
                print("res updated to:", leftMax + rightMax + root.val)
            self.res = max(leftMax + rightMax + root.val, self.res)
            return max(root.val + leftMax, root.val + rightMax)
        maxChild(root)
        return self.res