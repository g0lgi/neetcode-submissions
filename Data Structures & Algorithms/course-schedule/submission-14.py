class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_dict = {}
        visited = set()

        for k in range(len(prerequisites)):
            prerequisites_dict.setdefault(prerequisites[k][0], []).append(prerequisites[k][1])

        # print(prerequisites_dict)

        # visited = set()

        def dfs(curr_course: int, path: Set) -> bool:
            if curr_course in path:
                # print(prerequisites[course])
                # print(path)
                return False
            if curr_course in visited:
                return True
            else:
                path.add(curr_course)
                for curr_prereq in prerequisites_dict.get(curr_course, []):
                    # print(input)
                    temp = dfs(curr_prereq, path)
                    if temp == False:
                        return False
                    visited.add(curr_prereq)
                    # visited.add(tuple(prerequisites[j]))
                path.discard(curr_course)
                return True

        for course, prereqs in prerequisites_dict.items():
            temp = set()
            for prereq in prereqs:
                result = dfs(prereq, temp)
                if not result:
                    # print(i)
                    return False
            visited.add(course)

        return True
