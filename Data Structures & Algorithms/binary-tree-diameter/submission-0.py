# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        self.subTreeHeight(root)
        return self.maxDiameter
        
    def subTreeHeight(self, node):
        if node.left == None and node.right == None:
            return 0
        elif node.left == None:
            height = self.subTreeHeight(node.right) + 1
            self.maxDiameter = max(self.maxDiameter, height)
            return height
        elif node.right == None:
            height = self.subTreeHeight(node.left) + 1
            self.maxDiameter = max(self.maxDiameter, height)
            return height
        else:
            right = self.subTreeHeight(node.right)
            left = self.subTreeHeight(node.left)
            height = max(left + 1, right + 1)
            self.maxDiameter = max(self.maxDiameter, right + left + 2)
            return height