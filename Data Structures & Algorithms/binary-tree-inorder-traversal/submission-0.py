# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if root.left == None and root.right == None:
                return [root.val]
            elif root.right == None:
                return dfs(root.left) + [root.val]
            elif root.left == None:
                return [root.val] + dfs(root.right)
            else:
                return dfs(root.left) + [root.val] + dfs(root.right)

        if root == None:
            return []
        
        return dfs(root)