class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        counter = 1
        biggest = 1
        nums.sort()
        for i in range(len(nums) - 1): 
            incremental = (nums[i + 1] - nums[i] == 1)
            identical = (nums[i + 1] - nums[i] == 0)
            if incremental:
                counter += 1
            elif identical:
                continue
            else:
                counter = 1
            if counter > biggest:
                biggest = counter
            print(i, incremental, counter, biggest)
        return biggest