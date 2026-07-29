class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, [i, j]):
                        return True
        return False
                    
    def dfs(self, board: List[List[str]], word: str, current: List[int], visited=None) -> bool:
        if visited == None:
            visited = set()
        
        # ✅ FIXED
        r, c = current[0], current[1]

        # 1. Out-of-bounds check (MUST be first)
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return False

        # 2. Visited or character mismatch check
        if (r, c) in visited or board[r][c] != word[0]:
            return False
        
        if len(word) == 1:
            return True
        
        visited.add(tuple(current))
        
        found = (self.dfs(board, word[1:], [current[0] + 1, current[1]], visited) or self.dfs(board, word[1:], [current[0], current[1] + 1], visited) or self.dfs(board, word[1:], [current[0] - 1, current[1]], visited) or self.dfs(board, word[1:], [current[0], current[1] - 1], visited))

        visited.remove(tuple(current))

        return found