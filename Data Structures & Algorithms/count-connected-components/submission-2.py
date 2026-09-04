class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        prerequisites_dict = {}
        visited = set()

        for k in range(len(edges)):
            prerequisites_dict.setdefault(edges[k][0], set()).add(edges[k][1])
            prerequisites_dict.setdefault(edges[k][1], set()).add(edges[k][0])
            
        def dfs(node: int):
            visited.add(node)
            if node in prerequisites_dict:
                    for neighbor in prerequisites_dict[node]:
                        if neighbor in visited:
                            continue
                        dfs(neighbor)
                # prerequisites_dict.pop(node)

        counter = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                counter += 1

        return counter