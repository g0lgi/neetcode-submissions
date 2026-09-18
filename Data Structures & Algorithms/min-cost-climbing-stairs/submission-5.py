class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two_away = 0
        one_away = 0
        current = 0

        for i in range(len(cost) - 1, -1, -1):
            current = min(one_away, two_away) + cost[i]
            two_away = one_away
            one_away = current

        return min(one_away, two_away)
