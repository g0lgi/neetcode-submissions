# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))