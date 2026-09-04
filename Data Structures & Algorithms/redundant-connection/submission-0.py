class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        prerequisites_dict = {}

        answer = []

        def dfs(curr: int, target: int, visited: Set) -> bool:
            if curr in visited:
                return False
            if curr == target:
                return True
            if curr not in prerequisites_dict:
                return False
            result = False
            visited.add(curr)
            for neighbor in prerequisites_dict[curr]:
                result = result or dfs(neighbor, target, visited)
            return result
        
        for k in range(len(edges)):
            temp = set()
            if dfs(edges[k][0], edges[k][1], temp):
                answer = edges[k]
            else:
                prerequisites_dict.setdefault(edges[k][0], set()).add(edges[k][1])
                prerequisites_dict.setdefault(edges[k][1], set()).add(edges[k][0])
        
        return answer