class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return num
            unique_nums.add(num)