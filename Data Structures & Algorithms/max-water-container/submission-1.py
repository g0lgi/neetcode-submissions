class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        pointer1 = 0
        pointer2 = len(heights) - 1
        while pointer1 < pointer2:
            temp = min(heights[pointer1], heights[pointer2]) * abs(pointer2 - pointer1)
            print(temp, heights[pointer1], heights[pointer2])
            if temp > result:
                result = temp
            if heights[pointer1] < heights[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1
        return result
