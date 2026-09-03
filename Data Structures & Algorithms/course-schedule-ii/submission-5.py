class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisites_dict = {}
        visited = set()
        result = []

        for k in range(len(prerequisites)):
            prerequisites_dict.setdefault(prerequisites[k][0], []).append(prerequisites[k][1])

        # print(prerequisites_dict)

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
                path.discard(curr_course)
                visited.add(curr_course)
                result.append(curr_course)
                print("added " + str(curr_course) + " to results dari curr_course")
                return True

        for course, prereqs in prerequisites_dict.items():
            if course in visited:
                continue
            temp = set()
            for prereq in prereqs:
                not_cycle = dfs(prereq, temp)
                if not not_cycle:
                    # print(i)
                    return []
            visited.add(course)
            # print(course)
            result.append(course)
            # if len(result) == numCourses:
            #     return result
            print("added " + str(course) + " to results dari course")

        for course in range(numCourses):
            if course not in visited:
                result.append(course)
        return result