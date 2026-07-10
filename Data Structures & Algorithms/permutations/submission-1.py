class Solution:
    def permute(self, nums: List[int]) -> List[List[List[int]]]:
        output = []
        temp = []
        visited = [False] * len(nums)

        def dfs(i: int):
            # 1. Track entry into the function
            indent = "  " * len(temp)  # Visualizes recursion depth
            # print(f"{indent}--> Enter dfs(i={i}) | temp={temp} | visited={visited}")

            if len(temp) == len(nums):
                output.append(temp.copy())
                # print(f"{indent}    Found valid permutation! Added: {temp}")
                # Analyze what happens here: you return without resetting visited[i] or popping temp!
            else:
                for j in range(len(nums)):
                    if visited[j]:
                        continue
                    else:
                        visited[j] = True
                        temp.append(nums[j])
                        dfs(j)
                        visited[j] = False
                        temp.pop()
                        print(f"{indent}    Backtracked: temp={temp} | visited={visited}")
            return

        dfs(0)
        return output