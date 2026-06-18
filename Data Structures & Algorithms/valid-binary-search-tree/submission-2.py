# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root, minVal, maxVal):
            if root.left and root.right:
                if root.left.val > minVal and root.right.val < maxVal and root.left.val < root.val < root.right.val:
                    return valid(root.left, minVal, root.val) and valid(root.right, root.val, maxVal)
                else:
                    return False
            elif root.left:
                if root.left.val > minVal and root.left.val < root.val:
                    return valid(root.left, minVal, root.val)
                else:
                    return False
            elif root.right:
                if root.right.val < maxVal and root.val < root.right.val:
                    return valid(root.right, root.val, maxVal)
                else:
                    return False
            else:
                return True
        
        return valid(root, float('-inf'), float('inf'))