class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # you want to find the first letter
        # kick off a dfs / bfs from that letter
        i = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def dfs(i, r, c, visited):
            if i == len(word):
                return True
            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if (nx >= 0 and nx < len(board) and 
                    ny >= 0 and ny < len(board[0]) and 
                    (nx, ny) not in visited and
                    board[nx][ny] == word[i]):

                    visited.add((nx, ny))
                    if dfs(i + 1, nx, ny, visited):
                        return True
                    visited.remove((nx, ny))
            return False

        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[i]:
                    visited = set()
                    visited.add((r, c))
                    if dfs(i + 1, r, c, visited):
                        return True
        
        return False



                



            
        