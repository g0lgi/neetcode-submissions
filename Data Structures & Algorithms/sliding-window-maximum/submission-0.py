import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 1
        right = k
        result = []
        pq = []
        for i in range(k):
            heapq.heappush_max(pq,(nums[i], i))
        result.append(pq[0][0])
        while right < len(nums):
            heapq.heappush_max(pq,(nums[right], right))
            while pq[0][1] < left:
                heapq.heappop_max(pq)
            result.append(pq[0][0])
            right += 1
            left += 1
        return result