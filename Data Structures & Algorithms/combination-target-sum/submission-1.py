class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        sums = []
        rolling_sum = 0

        def dfs(i: int):
            nonlocal rolling_sum
            # print(f"At index {i}: rolling_sum={rolling_sum}, actual_sum={sum(sums)}, sums={sums}")
            # assert rolling_sum == sum(sums), "State desynchronized!"
            
            if rolling_sum == target:
                output.append(sums.copy())
                return
            
            if i >= len(nums):
                return

            if rolling_sum > target:
                return
            
            sums.append(nums[i])
            rolling_sum += nums[i]
            dfs(i)

            last = sums.pop()
            rolling_sum -= last
            dfs(i + 1)
        
        dfs(0)
        return output