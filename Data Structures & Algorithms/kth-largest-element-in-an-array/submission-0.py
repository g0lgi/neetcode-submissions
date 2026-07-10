import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        counter = 0
        while counter < (k - 1):
            heapq.heappop(max_heap)
            counter += 1
        return -heapq.heappop(max_heap)