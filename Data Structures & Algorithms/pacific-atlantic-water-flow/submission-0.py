class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # is_pac = True -> pac-bordering, False -> atl-bordering
        def dfs(x: int, y: int, ocean: Set):
            if (x, y) not in ocean:
                ocean.add((x, y))

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx = x + dx
                ny = y + dy
                if (
                    nx >= 0
                    and ny >= 0
                    and nx < len(heights)
                    and ny < len(heights[0])
                    and heights[nx][ny] >= heights[x][y]
                    and (nx, ny) not in ocean
                ):
                    ocean.add((nx, ny))
                    dfs(nx, ny, ocean)
        
        pac_border = set()
        atl_border = set()

        for i in range(len(heights)):
            dfs(i, 0, pac_border)
            dfs(i, len(heights[0]) - 1 - i, atl_border)

        for j in range(len(heights[0])):
            dfs(0, j, pac_border)
            dfs(len(heights) - 1, j, atl_border)

        return list(pac_border.intersection(atl_border))
