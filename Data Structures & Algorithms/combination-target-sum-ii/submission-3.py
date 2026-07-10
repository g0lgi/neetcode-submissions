class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        output = []

        sums = []
        rolling_sum = 0

        def dfs(i: int):
            nonlocal rolling_sum
            if rolling_sum == target:
                output.append(sums.copy())
                return
            
            if i >= len(candidates):
                return

            for j in range(i, len(candidates)):
                if rolling_sum + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                else:
                    sums.append(candidates[j])
                    rolling_sum += candidates[j]
                    dfs(j + 1)
                    rolling_sum -= sums.pop()

        dfs(0)

        # new_output = [list(t) for t in {tuple(i) for i in output}]
        return output