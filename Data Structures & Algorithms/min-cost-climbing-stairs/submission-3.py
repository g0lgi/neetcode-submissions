class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * (len(cost) + 2) # memo[i] is most efficient total cost up to i, filled from right to left
        memo[-1] = 0
        memo[-2] = 0

        # print(len(cost), len(memo))

        def recursion(curr_step: int):
            if memo[curr_step] != -1:
                return
            if curr_step < 0:
                return
            memo[curr_step] = min(memo[curr_step + 1], memo[curr_step + 2]) + cost[curr_step]
            # print(curr_step, memo[curr_step])
            recursion(curr_step - 1)
            recursion(curr_step - 2)

        recursion(len(cost) - 1)
        # print(memo)
        return min(memo[0], memo[1])