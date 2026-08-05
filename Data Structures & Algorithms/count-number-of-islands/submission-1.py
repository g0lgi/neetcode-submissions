class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited_matrix = [
    [False for _ in range(len(grid[0]))]
    for _ in range(len(grid))
]

        output = 0

        def dfs(i: int, j: int):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0' or visited_matrix[i][j]:
                return
            
            visited_matrix[i][j] = True

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and not visited_matrix[i][j]:
                    dfs(i, j)
                    output += 1
                    print(visited_matrix)
                    print('=============')
        
        return output