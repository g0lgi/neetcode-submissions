# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes = []
        # self.counter = 0
        def printInorder(root: Optional[TreeNode]):
            if root:
                # First recur on left child
                printInorder(root.left)
                # then print the data of node
                if len(self.nodes) < k:
                    self.nodes.append(root.val)
                else:
                    return self.nodes[k - 1]
                # now recur on right child
                printInorder(root.right)
        printInorder(root)
        return self.nodes[k - 1]
