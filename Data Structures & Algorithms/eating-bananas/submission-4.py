import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[-1]
        mid = int((left + right) / 2)
        k = 1
        while left <= right:
            mid = int((left + right) / 2)
            time = 0
            for j in range(len(piles)):
                time += math.ceil((piles[j] / mid))
            print(left, mid, right, time)
            if time <= h:
                k = mid
                right = mid - 1
            elif time > h:
                left = mid + 1
        return k