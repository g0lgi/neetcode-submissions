# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        mid = slow.next
        current = mid
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        # print(prev.val)
        slow.next = None
        while prev:
            # print(stack[-1].val)
            temp = head.next
            head.next = prev
            prev = prev.next
            head = head.next
            # print(head.val)
            head.next = temp
            head = head.next
            # print(head.val)
            # print("============")
        # print(stack)
        # print(slow.val)