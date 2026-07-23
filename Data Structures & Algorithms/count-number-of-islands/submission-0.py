from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # when you find a 1, run BFS to find all the adjacent 1s and mark them visited
        # continue traversing until you finish the graph
        visited = set()
        ans = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(start):
            queue = deque()
            queue.append((start[0], start[1]))
            visited.add((start[0], start[1]))

            while queue:
                curr_x, curr_y = queue.popleft()
                visited.add((curr_x, curr_y))
                for dx, dy in directions:
                    x, y = curr_x + dx, curr_y + dy
                    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != "1" or (x, y) in visited:
                        continue
                    else:
                        visited.add((x, y))
                        queue.append((x, y))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    ans += 1
                    bfs((r, c))
        
        return ans
                    

