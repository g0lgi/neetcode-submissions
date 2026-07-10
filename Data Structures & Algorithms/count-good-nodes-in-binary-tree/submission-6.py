# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, root.val)
        return self.result
    
    def dfs(self, node:Optional[TreeNode], curr_max: int):
        if not node:
            return
        if node.val >= curr_max:
            print(node.val, curr_max)
            self.result += 1
            self.dfs(node.left, node.val)
            self.dfs(node.right, node.val)
        else:
            self.dfs(node.left, curr_max)
            self.dfs(node.right, curr_max)