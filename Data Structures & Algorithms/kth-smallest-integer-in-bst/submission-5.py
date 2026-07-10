# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # self.nodes = []
        self.counter = 0
        self.result = -1
        def printInorder(node: Optional[TreeNode]):
            if node:
                # First recur on left child
                printInorder(node.left)
                # then print the data of node
                self.counter += 1
                if self.counter == k:
                    self.result = node.val
                    return
                # now recur on right child
                printInorder(node.right)
        printInorder(root)
        return self.result