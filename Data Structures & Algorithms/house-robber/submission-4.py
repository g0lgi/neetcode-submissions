class Solution:
    def rob(self, nums: List[int]) -> int:
        maxes = [0] * len(nums)
        # visited = [False] * len(nums)

        def recursion(curr_index: int) -> int:
            if curr_index < 0 or curr_index >= len(nums):
                return 0

            # if visited[curr_index]:
            #     return 0

            # visited[curr_index] = True
            # print(visited)
            

            if maxes[curr_index] == 0:
                print(curr_index)
                maxes[curr_index] = max(
                nums[curr_index]
                + recursion(curr_index + 2),
                recursion(curr_index + 1)
            )
            return maxes[curr_index]

        # result = recursion(0)

        # print(maxes)
        return recursion(0)
