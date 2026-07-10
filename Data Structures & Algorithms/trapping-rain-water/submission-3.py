class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        for i in range (1, len(height) - 1):
            maxHeightLeft = height[i]
            pointerLeft = i - 1
            while (pointerLeft >= 0):
                if height[pointerLeft] > maxHeightLeft:
                    maxHeightLeft = height[pointerLeft]
                pointerLeft -= 1
            maxHeightRight = height[i]
            pointerRight = i + 1
            while (pointerRight < len(height)):
                if height[pointerRight] > maxHeightRight:
                    maxHeightRight = height[pointerRight]
                pointerRight += 1
            result += min(maxHeightLeft, maxHeightRight) - height[i]
            print(height[i], maxHeightLeft, maxHeightRight, result)
        return result