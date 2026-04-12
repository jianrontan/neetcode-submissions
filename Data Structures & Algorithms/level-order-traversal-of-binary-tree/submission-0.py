# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self.levels(root, 0)
        return self.res

    def levels(self, root: Optional[TreeNode], level) -> None:
        if level >= len(self.res):
            self.res.append([])
        self.res[level].append(root.val)
        if root.left:
            self.levels(root.left, level + 1)
        if root.right:
            self.levels(root.right, level + 1)