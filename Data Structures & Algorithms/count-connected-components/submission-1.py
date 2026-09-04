class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        prerequisites_dict = {}
        visited = set()

        for k in range(len(edges)):
            prerequisites_dict.setdefault(edges[k][0], set()).add(edges[k][1])
            prerequisites_dict.setdefault(edges[k][1], set()).add(edges[k][0])
            
        def dfs(node: int):
            visited.add(node)
            for neighbor in prerequisites_dict[node]:
                if neighbor in visited:
                    continue
                dfs(neighbor)
            prerequisites_dict.pop(node)

        counter = 0
        while len(list(prerequisites_dict.keys())) >= 1:
            dfs(list(prerequisites_dict.keys())[0])
            counter += 1

        if len(visited) < n:
            counter += n - len(visited)

        return counter