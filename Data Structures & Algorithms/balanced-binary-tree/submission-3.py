# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.maxDepth(root)
        return self.balanced
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        if abs(left_height - right_height) > 1:
            self.balanced = False
        return 1 + max(left_height, right_height)