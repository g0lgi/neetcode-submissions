class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = [1]
        for i in range(0, len(nums) - 1):
            prefix_sum.append(prefix_sum[i] * nums[i])

        suffix_sum = 1
        for i in range(len(nums) - 1, 0, -1):
            prefix_sum[i] = prefix_sum[i] * suffix_sum
            suffix_sum = suffix_sum * nums[i]
        prefix_sum[0] = suffix_sum
        
        return prefix_sum