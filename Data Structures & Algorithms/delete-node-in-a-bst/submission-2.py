# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        prev = TreeNode(left=root)
        node = root
        while True:
            if not node:
                return root
            if key < node.val:
                prev = node
                node = node.left
            elif key > node.val:
                prev = node
                node = node.right
            else:
                break
        
        if node.left and node.right:
            left = node.right
            while True:
                if left.left:
                    left = left.left
                else:
                    break
            
            if prev.left == node:
                prev.left = node.right
            else:
                prev.right = node.right
            
            left.left = node.left
        elif node.left:
            if prev.left == node:
                prev.left = node.left
            else:
                prev.right = node.left
        elif node.right:
            if prev.left == node:
                prev.left = node.right
            else:
                prev.right = node.right
        else:
            if prev.left == node:
                prev.left = None
            else:
                prev.right = None
        
        return prev.left if root.val == key else root