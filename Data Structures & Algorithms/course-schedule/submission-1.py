class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # creating the graph
        graph = {course:[] for course in range(numCourses)}
        for pre in prerequisites:
            course = pre[0]
            prereq = pre[1]
            if prereq in graph:
                graph[prereq].append(course)
            else:
                graph[prereq] = [course]

        # you want to make sure you can reach every course with no cycles
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True
            
            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            graph[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True