import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1
        my_list = [(v, k) for k, v in dict1.items()]
        hq.heapify_max(my_list)
        i = 0
        result = []
        while i < k:
            result.append(heapq.heappop_max(my_list)[1])
            i += 1
        return result