# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        stack = []
        counter = 0

        while fast and fast.next:
            slow = slow.next
            counter += 1
            fast = fast.next.next
        mid = slow.next
        while mid:
            stack.append(mid)
            mid = mid.next

        # print(slow.val)
        # print(counter)
        # print(len(stack))

        slow.next = None
        while len(stack) != 0:
            # print(stack[-1].val)
            temp = head.next
            head.next = stack.pop()
            head = head.next
            # print(head.val)
            head.next = temp
            head = head.next
            print(head.val)
            # print("============")
        # print(stack)
        # print(slow.val)