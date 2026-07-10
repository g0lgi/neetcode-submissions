import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = []
        for stone in stones:
            heapq.heappush(min_heap, -stone)
        while len(min_heap) > 1:
            stone_1 = heapq.heappop(min_heap)
            # print(stone_1)
            stone_2 = heapq.heappop(min_heap)
            # print(stone_2)
            result = abs(stone_1 - stone_2)
            # print(result)
            if result > 0:
                heapq.heappush(min_heap, -result)
            # print(min_heap)
        if len(min_heap) > 0:
            return -min_heap[0]
        else:
            return 0