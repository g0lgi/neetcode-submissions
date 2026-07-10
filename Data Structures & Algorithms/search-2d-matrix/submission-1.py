class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y_left = 0
        y_right = len(matrix) - 1
        y_mid = int((y_right + y_left) / 2)
        while y_left <= y_right:
            y_mid = int((y_right + y_left) / 2)
            print(y_left, y_mid, y_right)
            if matrix[y_mid][0] == target:
                return True
            elif matrix[y_mid][0] < target:
                y_left = y_mid + 1
            elif matrix[y_mid][0] > target:
                y_right = y_mid - 1
        print(y_mid)
        if matrix[y_mid][0] > target:
            y_mid -= 1
        x_left = 0
        x_right = len(matrix[y_mid]) - 1
        x_mid = int((x_right + x_left) / 2)
        while x_left <= x_right:
            x_mid = int((x_right + x_left) / 2)
            print(x_left, x_mid, x_right)
            if matrix[y_mid][x_mid] == target:
                return True
            elif matrix[y_mid][x_mid] < target:
                x_left = x_mid + 1
            elif matrix[y_mid][x_mid] > target:
                x_right = x_mid - 1
        return False
        