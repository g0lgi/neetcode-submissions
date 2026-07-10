class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = [1]
        for i in range(0, len(nums) - 1):
            prefix_sum.append(prefix_sum[i] * nums[i])
        print(prefix_sum)

        suffix_sum = [1]
        for i in range(len(nums) - 1, 0, -1):
            suffix_sum.append(nums[i] * suffix_sum[-1])
        print(suffix_sum)
        output = []
        for i in range(len(nums)):
            output.append(prefix_sum[i] * suffix_sum[-i - 1])
        return output