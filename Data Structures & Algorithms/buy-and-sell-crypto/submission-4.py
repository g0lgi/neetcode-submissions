class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = 101
        result = 0

        for i in range(len(prices)):
            if (prices[i] - current_min) > result:
                result = prices[i] - current_min
            if prices[i] < current_min:
                current_min = prices[i]
        return result