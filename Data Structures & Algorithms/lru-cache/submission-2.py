class ListNode:
    def __init__(self, val=[], next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        head_node = ListNode()
        tail_node = ListNode()
        
        head_node.next = tail_node
        tail_node.prev = head_node

        self.head = head_node
        self.tail = tail_node

    def get(self, key: int) -> int:
        result = self.cache.get(key, -1)
        
        if result == -1:
            return result
        if len(self.cache) == 1:
            return result
        
        curr = self.head
        while curr and curr.val[0] != key:
            curr = curr.next
        
        if curr == self.tail:
            return result
        
        if curr == self.head:
            self.head = self.head.next
            curr.next.prev = None
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        
        curr.prev = self.tail
        self.tail.next = curr
        self.tail = curr
        
        return result

    def put(self, key: int, value: int) -> None:
        result = self.cache.get(key, -1)
        
        if result == -1:
            node = ListNode([key, value])
            if not self.head.val:
                self.head = node
                self.tail = node
            else:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.pop(self.head.val[0])
                self.head = self.head.next
                self.head.prev = None
            return
        else:
            curr = self.head
            while curr and curr.val[0] != key:
                curr = curr.next
            
            curr.val[1] = value
            self.cache[key] = value
            if len(self.cache) == 1 or curr == self.tail:
                return

            if curr == self.head:
                self.head = self.head.next
                curr.next.prev = None
            else:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            
            curr.prev = self.tail
            self.tail.next = curr
            self.tail = curr
        