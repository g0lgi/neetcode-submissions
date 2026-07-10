# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.max_diameter
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        d = left_height + right_height
        if d > self.max_diameter:
            self.max_diameter = d
        
        return 1 + max(left_height, right_height)
