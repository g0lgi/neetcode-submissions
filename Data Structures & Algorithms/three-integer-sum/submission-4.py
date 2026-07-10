class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            pointer1 = i + 1
            pointer2 = len(nums) - 1
            target = -nums[i]
            while pointer1 < pointer2:            
                temp = nums[pointer1] + nums[pointer2]
                if temp > target:
                    pointer2 -= 1
                elif temp < target:
                    pointer1 += 1
                elif temp == target:
                    result.append([nums[i], nums[pointer1], nums[pointer2]])
                    while pointer1 < pointer2 and nums[pointer2] == nums[pointer2 - 1]:
                        pointer2 -= 1
                    pointer2 -= 1
                    while pointer1 < pointer2 and nums[pointer1] == nums[pointer1 + 1]:
                        pointer1 += 1
                    pointer1 += 1
        return result