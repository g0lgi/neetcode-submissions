class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents = [i for i in range(len(points))]
        rank = [0] * (len(points))

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            # If they share the same root, they are already in the same set
            if root_x == root_y:
                return False

            # Union by Rank optimization
            if rank[root_x] < rank[root_y]:
                parents[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parents[root_y] = root_x
            else:
                parents[root_y] = root_x
                rank[root_x] += 1

            return True

        edges = []
        for i in range(len(points)):
            for j in range(len(points)):
                edges.append(
                    [abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j]
                )
        
        edges = sorted(edges)
        
        total_cost = 0
        count = 0
        for cost, point_1, point_2 in edges:
            if find(point_1) != find(point_2):
                union(point_1, point_2)
                total_cost += cost
                count += 1

                if count == len(points) - 1:
                    break
        
        return total_cost