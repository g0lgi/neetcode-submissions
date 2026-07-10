class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        counter = 1
        biggest = 1
        my_set = set(nums)
        for i in range(len(nums)): 
            counter = 1
            current = nums[i]
            if (current - 1) in my_set:
                while (current - 1) in my_set:
                    counter += 1
                    current -= 1
            if counter > biggest:
                biggest = counter
            print(i, current, counter, biggest)
        return biggest