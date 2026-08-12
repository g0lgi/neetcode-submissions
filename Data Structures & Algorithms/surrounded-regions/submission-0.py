from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def bfs(i: int, j: int):
            q = deque()
            q.append((i, j))

            while q:
                r, c = q.popleft()
                board[r][c] = 'T'

                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr = r + dx
                    nc = c + dy

                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 'O':
                        q.append((nr, nc))
        
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                bfs(0, i)
            if board[len(board) - 1][i] == 'O':
                bfs(len(board) - 1, i)
        for j in range(len(board)):
            if board[j][0] == 'O':
                bfs(j, 0)
            if board[j][len(board[0]) - 1] == 'O':
                bfs(j, len(board[0]) - 1)
        
        for k in range(len(board)):
            for l in range(len(board[k])):
                if board[k][l] == 'T':
                    board[k][l] = 'O'
                elif board[k][l] == 'O':
                    board[k][l] = 'X'
            
# go around the board to find any O at its sides
# do bfs for each O to find any other O connected to it, mark them as e.g, T
# if all the sides of the board are traversed, do another run and mark all remaining O's as X (theyre all surrounded)
# rename T's as O