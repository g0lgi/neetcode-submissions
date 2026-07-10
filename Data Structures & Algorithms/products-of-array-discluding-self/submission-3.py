class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] * nums[i])
        del prefix_sum[-1]
        prefix_sum.insert(0, 1)
        
        suffix_sum = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            suffix_sum.append(nums[i] * suffix_sum[-1])
        del suffix_sum[-1]
        suffix_sum.insert(0, 1)

        output = []
        for i in range(len(nums)):
            output.append(prefix_sum[i] * suffix_sum[-i - 1])
        return output