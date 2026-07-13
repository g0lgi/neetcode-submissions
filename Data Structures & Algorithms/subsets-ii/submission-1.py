class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        # output.append([])

        subset = []
        def dfs(i: int):
            output.append(subset.copy())
                
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                subset.append(nums[j])
                dfs(j + 1)
                subset.pop()
            
            return
        
        dfs(0)
        return list(output)