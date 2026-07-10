# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes = []
        self.target = k
        self.printInorder(root)
        return self.nodes[k - 1]
    
    def printInorder(self, root: Optional[TreeNode]):
        if root:
            # First recur on left child
            self.printInorder(root.left)
            # then print the data of node
            if len(self.nodes) == self.target:
                return
            self.nodes.append(root.val)
            # now recur on right child
            self.printInorder(root.right)
