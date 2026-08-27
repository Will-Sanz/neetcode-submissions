class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        max_area = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            area = 0

            while queue:
                x, y = queue.popleft()
                area += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if (nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0])
                        or grid[nx][ny] == 0 or (nx, ny) in visited):
                        continue

                    queue.append((nx, ny))
                    visited.add((nx, ny))
        
            return area
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] not in visited and grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area