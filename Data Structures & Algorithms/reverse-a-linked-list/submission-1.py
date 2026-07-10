# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head # 0

        while current:
            temp = current.next # temp = 1
            current.next = prev # 0.next = None
            prev = current # prev = 0
            current = temp # current = 1
        return prev