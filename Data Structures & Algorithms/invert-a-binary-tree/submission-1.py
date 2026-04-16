# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def invert(root: Optional[TreeNode]) -> None:
            if root.left and root.right:
                newRight = root.left
                root.left = root.right
                root.right = newRight
                invert(root.left)
                invert(root.right)
            elif root.left:
                root.right = root.left
                root.left = None
                invert(root.right)
            elif root.right:
                root.left = root.right
                root.right = None
                invert(root.left)

        invert(root)
        return root