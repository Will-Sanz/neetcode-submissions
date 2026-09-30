from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # start at the treasure chest and bfs outwards
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or
                    nr >= len(grid) or nc >= len(grid[0])
                    or grid[nr][nc] != 2147483647):
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))