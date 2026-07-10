class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {} # hold value as key and index as value
        for i in range(len(nums)):
            if (target - nums[i]) in dict1:
                return [dict1.get(target - nums[i]), i]
            else:
                dict1[nums[i]] = i
            