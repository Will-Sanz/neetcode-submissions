class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # for a valid tree, the graph has to be connected and no cycles
        # dfs to make sure there are no cycles and we visit every node
        graph = defaultdict(list)
        for edge1, edge2 in edges:
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)

        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                elif neighbor in visited:
                    return False
                else:
                    if not dfs(neighbor, node):
                        return False
            return True

        return dfs(0, -1) and len(visited) == n