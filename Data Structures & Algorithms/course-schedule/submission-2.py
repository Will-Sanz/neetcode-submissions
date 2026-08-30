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
        visiting = set()
        visited = set()
        
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True