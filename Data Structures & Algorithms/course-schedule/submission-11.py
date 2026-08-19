class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_dict = {}
        visited = set()

        for k in range(len(prerequisites)):
            prerequisites_dict.setdefault(prerequisites[k][0], []).append(prerequisites[k][1])

        print(prerequisites_dict)

        # visited = set()

        def dfs(prereq: List[int], path: Set) -> bool:
            if tuple(prereq) in path:
                # print(prerequisites[course])
                # print(path)
                return False
            if tuple(prereq) in visited:
                return True
            else:
                path.add(tuple(prereq))
                for p2 in prerequisites_dict.get(prereq[1], []):
                    inputt = [prereq[1], p2]
                    # print(input)
                    temp = dfs(inputt, path)
                    if temp == False:
                        return False
                    visited.add(tuple(inputt))
                    # visited.add(tuple(prerequisites[j]))
                path.discard(tuple(prereq))
                return True

        for i in range(len(prerequisites)):
            temp = set()
            result = dfs(prerequisites[i], temp)
            visited.add(tuple(prerequisites[i]))
            if not result:
                # print(i)
                return False

        return True
