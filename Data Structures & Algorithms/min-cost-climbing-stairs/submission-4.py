class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two_away = 0
        one_away = 0
        current = 0

        for index, item in reversed(list(enumerate(cost))):
            current = min(one_away, two_away) + item
            two_away = one_away
            one_away = current

        return min(one_away, two_away)
