import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1
        bucket_sort_list = []
        i = 0
        while i <= len(nums):
            bucket_sort_list.append([])
            i += 1
        for key, value in dict1.items():
            bucket_sort_list[value].append(key)
        j = len(bucket_sort_list)
        result = []
        while True:
            if len(bucket_sort_list[j - 1]) != 0:
                for answer in bucket_sort_list[j - 1]:
                    result.append(answer)
                    if len(result) == k:
                        return result
            j -= 1