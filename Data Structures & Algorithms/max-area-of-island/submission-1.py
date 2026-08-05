class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        visited_matrix = [
    [False for _ in range(len(grid[0]))]
    for _ in range(len(grid))
]

        output = 0

        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0 or visited_matrix[i][j]:
                return 0
            
            visited_matrix[i][j] = True

            return 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and not visited_matrix[i][j]:
                    temp = dfs(i, j)
                    # print(temp)
                    if temp > output:
                        output = temp
                    # print(visited_matrix)
                    # print('=============')
        
        return output