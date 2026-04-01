# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        if p.val < q.val:
            left = p
            right = q
        else:
            left = q
            right = p
        while not (left.val < cur.val and right.val > cur.val):
            if left.val == cur.val:
                return left
            elif right.val == cur.val:
                return right
            elif left.val < cur.val and right.val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return cur