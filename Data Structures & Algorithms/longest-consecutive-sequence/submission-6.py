class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        biggest = 1
        my_set = set(nums)
        for i in range(len(nums)): 
            current = nums[i]
            if (current - 1) not in my_set:
                counter = 1
                while (current + 1) in my_set:
                    counter += 1
                    current += 1
                if counter > biggest:
                    biggest = counter
        return biggest