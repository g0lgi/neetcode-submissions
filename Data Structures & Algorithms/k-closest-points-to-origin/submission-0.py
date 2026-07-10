import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_distance_pairs_heap = []
        for i in range(len(points)):
            heapq.heappush(point_distance_pairs_heap, (math.sqrt(points[i][0]**2 + points[i][1]**2), i))
        
        result = []
        for j in range(k):
            _, index = heapq.heappop(point_distance_pairs_heap)
            result.append(points[index])
        return result