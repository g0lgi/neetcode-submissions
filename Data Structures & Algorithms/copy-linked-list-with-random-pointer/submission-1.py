"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        result = Node(head.val, None, head.random)
        result_head = result
        mapper = {head: result_head}
        current = head.next
        while current:
            temp = Node(current.val, None, current.random)
            result.next = temp 
            result = result.next
            mapper[current] = result
            current = current.next
        result = result_head
        print(mapper)
        while result:
            result.random = mapper.get(result.random, None)
            result = result.next
        return result_head