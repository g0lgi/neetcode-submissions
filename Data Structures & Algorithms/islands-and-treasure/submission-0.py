from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j))

        counter = 0

        while q:
            level_size = len(q)

            for _ in range(level_size):
                curr = q.popleft()

                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    r, c = curr[0] + dx, curr[1] + dy

                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] > grid[curr[0]][curr[1]] + 1:
                        grid[r][c] = grid[curr[0]][curr[1]] + 1
                        q.append((r, c))

            counter += 1
