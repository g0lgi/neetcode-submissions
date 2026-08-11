from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        fresh_fruit_present = False

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh_fruit_present = True
        
        if not fresh_fruit_present:
            return 0

        counter = 0

        while q:
            level_size = len(q)

            for _ in range(level_size):
                curr = q.popleft()

                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    r, c = curr[0] + dx, curr[1] + dy

                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))

            print(q)
            print(grid)
            counter += 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        
        return counter - 1
