# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def left(root):
            if not root:
                return
            res.append(root.val)
            if root.left and root.right:
                left(root.left)
                left(root.right)
            elif root.left:
                left(root.left)
            elif root.right:
                left(root.right)
        
        left(root)
        return res