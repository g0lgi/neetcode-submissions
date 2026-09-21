class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxes = [0] * len(nums)

        def recursion(curr_index: int, first_house_robbed: bool) -> int:
            if curr_index < 0 or curr_index >= len(nums):
                return 0

            if curr_index == (len(nums) - 1) and first_house_robbed:
                print(maxes)
                return 0

            if maxes[curr_index] == 0:
                # print(curr_index)
                maxes[curr_index] = max(
                    nums[curr_index] + recursion(curr_index + 2, first_house_robbed),
                    recursion(curr_index + 1, first_house_robbed),
                )
            return maxes[curr_index]

        # temp_nums = nums.copy()
        # nums = nums[0:-1]
        result1 = recursion(0, True)
        # print(maxes)
        # print(nums, result1)

        # nums = temp_nums.copy()
        # nums = nums[1:]
        maxes = [0] * len(nums)
        result2 = recursion(1, False)
        # print(nums, result2)
        return max(result1, result2)
