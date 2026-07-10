# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result_head = result
        carryover = 0

        while l1 and l2:
            addition_result = l1.val + l2.val + carryover
            carryover = int(addition_result / 10)
            new = ListNode(addition_result % 10)
            result.next = new
            result = result.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            addition_result = l1.val + carryover
            carryover = int(addition_result / 10)
            new = ListNode(addition_result % 10)
            result.next = new
            result = result.next
            l1 = l1.next
        
        while l2:
            addition_result = l2.val + carryover
            carryover = int(addition_result / 10)
            new = ListNode(addition_result % 10)
            result.next = new
            result = result.next
            l2 = l2.next
        
        if carryover:
            new = ListNode(carryover)
            result.next = new
            result = result.next
        
        return result_head.next