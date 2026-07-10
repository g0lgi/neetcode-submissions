class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1
        sorted_array = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
        i = 0
        result = []
        while i < k:
            result.append(sorted_array[i][0])
            i += 1
        return result