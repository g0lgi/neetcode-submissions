# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfsHelper(root, -1001, 1001)
        
    def dfsHelper(self, root: Optional[TreeNode], curr_min: int, curr_max: int) -> bool:
        if not root:
            return True
        # if bool(root.left) != bool(root.right):
        #     return False
        if curr_min < root.val < curr_max:
                return self.dfsHelper(root.left, curr_min, root.val) and self.dfsHelper(root.right, root.val, curr_max)
        else:
            # print('1')
            return False