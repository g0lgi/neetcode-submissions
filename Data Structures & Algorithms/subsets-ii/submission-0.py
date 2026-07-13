class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()

        subset = []
        def dfs(i: int):
            if i >= len(nums):
                output.add(tuple(subset.copy()))
                return
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return list(output)