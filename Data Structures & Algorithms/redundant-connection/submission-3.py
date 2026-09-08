class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

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

        answer = []

        for edge in edges:
            if (find(edge[0]) == find(edge[1])):
                answer = edge
            cycle = union(edge[0], edge[1])
        return answer