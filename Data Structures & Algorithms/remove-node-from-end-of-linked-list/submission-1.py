# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size_of_list = 0
        traverse = head
        while traverse:
            traverse = traverse.next
            size_of_list += 1
        
        target = size_of_list - n
        print(target, size_of_list, n)
        counter = 0
        current = head
        prev = None
        while counter < target:
            prev = current
            current = current.next
            counter += 1

        if prev == None:
            head = current.next
        else:
            prev.next = current.next
        

        return head