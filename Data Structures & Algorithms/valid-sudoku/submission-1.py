class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for a in range(9):
            row_duplicates = set()
            # print(f"--- Checking Row {a} ---")
            for b in range(9):
                if board[a][b] != ".":
                    if board[a][b] in row_duplicates:
                        print(f"Row {a} Error: Found duplicate {board[a][b]} at index ({a}, {b})")
                        return False
                    row_duplicates.add(board[a][b])
            
            column_duplicates = set()
            # print(f"--- Checking Column {a} ---")
            for c in range(9):
                if board[c][a] != ".":
                    if board[c][a] in column_duplicates:
                        print(f"Column {a} Error: Found duplicate {board[c][a]} at index ({c}, {a})")
                        return False
                    column_duplicates.add(board[c][a])
        
        coords = [0, 3, 6]
        for e in range(0, 3):
            row_start = e * 3
            for col_start in coords:
                # print(f"--- Checking 3x3 Box (Start Row: {row_start}, Start Col: {col_start}) ---")
                square_duplicates = set()
                
                for f in range(row_start, row_start + 3):
                    for g in range(col_start, col_start + 3):
                        # print(f"  Scanning cell: ({f}, {g})") 
                        
                        if board[f][g] != ".":
                            if board[f][g] in square_duplicates:
                                # print(f"Box Error: Found duplicate {board[f][g]} at ({f}, {g})")
                                return False
                            else:
                                square_duplicates.add(board[f][g]) 
        return True