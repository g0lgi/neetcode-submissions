class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for j in range(len(nums)):
            if (target - nums[j]) in nums_dict and nums_dict[target - nums[j]] != j:
                return [j, nums_dict[target - nums[j]]]