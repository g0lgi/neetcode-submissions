class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # pq = []
        # pq.append(0)

        distances = [math.inf] * len(points)
        distances[0] = 0
        visited = [False] * len(points)
        result = 0

        for _ in range(len(points)):
            # print(distances)
            curr = -1
            for i in range(len(distances)):
                if not visited[i] and (curr == -1 or distances[i] < distances[curr]):
                    curr = i

            visited[curr] = True

            for j in range(len(points)):
                if visited[j]:
                    continue
                curr_distance = abs(points[curr][0] - points[j][0]) + abs(points[curr][1] - points[j][1])
                if curr_distance < distances[j]:
                    distances[j] = curr_distance
                    
            result += distances[curr]

        return result