from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # you want to count the number of levels the bfs goes through
        # multi-source BFS from every starting rotten orange

        queue = deque()
        visited = set()
        time = 0
        fresh = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r, c])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # check bounds and fresh
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1


        

        
            
                




        
        