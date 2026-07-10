# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return []
        bfs = []
        result = 1
        queue = deque()
        queue.append((root, root.val))
        while len(queue) > 0:
            nodes_in_level = []
            for i in range(len(queue)):
                curr, curr_max = queue.popleft()
                if curr:
                    if len(bfs) > 0:
                        print(bfs)
                        print(nodes_in_level)
                        if curr.val >= curr_max:
                            result += 1
                    nodes_in_level.append(curr.val)
                if curr.left:
                    queue.append((curr.left, max(curr_max, curr.left.val)))
                if curr.right:
                    queue.append((curr.right, max(curr_max, curr.right.val)))
            bfs.append(nodes_in_level)
        # print(bfs)
        return result