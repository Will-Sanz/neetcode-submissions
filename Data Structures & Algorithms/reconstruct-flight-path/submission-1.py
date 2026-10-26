from collections import defaultdict
from collections import deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)
        for start in graph:
            graph[start].sort(reverse=True)
        
        stack = ["JFK"]
        res = []

        while stack:
            curr = stack[-1]

            if graph[curr]:
                stack.append(graph[curr].pop())
            else:
                res.append(stack.pop())
        return res[::-1]

        


        
