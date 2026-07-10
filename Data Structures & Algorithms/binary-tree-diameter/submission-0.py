# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d = self.maxDepth(root.left) + self.maxDepth(root.right)
        if d > self.max_diameter:
            self.max_diameter = d
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.max_diameter
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
