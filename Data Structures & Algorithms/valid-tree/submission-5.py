class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 1:
            return True
        if len(edges) != n - 1:
            return False
        prerequisites_dict = {}
        visited = set()

        for k in range(len(edges)):
            prerequisites_dict.setdefault(edges[k][0], set()).add(edges[k][1])
            prerequisites_dict.setdefault(edges[k][1], set()).add(edges[k][0])

        def dfs(curr: int, parent: int | None) -> bool:
            if curr in visited and curr != parent:
                # print(prerequisites[course])
                # print(path)
                return False
            visited.add(curr)
            for curr_prereq in prerequisites_dict.get(curr, []):
                if curr_prereq == parent:
                    continue
                temp = dfs(curr_prereq, curr)
                if temp == False:
                    # print(curr, curr_prereq)
                    # print(visited)
                    return False
            return True

        no_cycle = dfs(list(prerequisites_dict.keys())[0], None)
        if not no_cycle or len(visited) != n:
            print(prerequisites_dict)
            return False
        else:
            return True