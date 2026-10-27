from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
                # dfs - return False if cycle, return True otherwise
        # visited, visiting, and order sets to track cycles and result

        visited, visiting = set(), set()
        order = []

        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            # if you're checking if all a courses dependencies are gone, then you flip graph order
            for dep in graph[course]:
                if dep in visiting:
                    return False
                if not dfs(dep):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            # append a course if all it's dependencies are clear
            order.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order[::-1]


