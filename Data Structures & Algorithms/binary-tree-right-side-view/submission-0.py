# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.result = []
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            nodes_in_level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                nodes_in_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            self.result.append(nodes_in_level[-1])
        return self.result