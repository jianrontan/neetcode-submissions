# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        arr = []
        def levels(root: Optional[TreeNode], level) -> None:
            if level > len(arr) - 1:
                arr.append([root.val])
            else:
                arr[level].append(root.val)
            if root.left:
                levels(root.left, level + 1)
            if root.right:
                levels(root.right, level + 1)
        levels(root, 0)

        res = []
        for l in arr:
            res.append(l[-1])
        return res