from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # graph that maps (prereq -> the courses it frees)
        for course, pre in prerequisites:
            graph[pre].append(course)

        visiting, visited = set(), set()
        res = []

        # returns True if you explore without finding a cycle, False otherwise
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)

            for neighbor in graph[course]:
                if neighbor in visiting:
                    return False
                if not dfs(neighbor):
                    return False

            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res[::-1]


