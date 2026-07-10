class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        heights.append(0)
        largest = 0
        stack = []
        default_left = -1
        for i in range(len(heights)):
            if len(stack) == 0 and heights[i] != 0:
                stack.append(i)
            else:
                while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                    temp_index = stack[-1]
                    stack.pop()
                    if len(stack) > 0:
                        left = stack[-1]
                    else:
                        left = default_left
                    largest = max(largest, heights[temp_index] * (i - left - 1))
                    print(i, temp_index, left, largest)
                if heights[i] != 0:
                    stack.append(i)
                print(stack)
            if heights[i] == 0:
                default_left = i
        return largest