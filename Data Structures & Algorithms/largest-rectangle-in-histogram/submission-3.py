class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        for i in range(len(heights)):
            left = 1
            while ((i - left) >= 0) and (heights[i - left] >= heights[i]):
                left += 1
            right = 1
            while ((i + right) < len(heights)) and (heights[i + right] >= heights[i]):
                right += 1
            largest = max(largest, heights[i] * (1 + (left + right - 2)))
            print(i, largest, left, right)
        return largest
