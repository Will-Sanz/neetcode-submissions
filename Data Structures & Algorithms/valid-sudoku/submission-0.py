class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        row, col = defaultdict(list), defaultdict(list)
        quad = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r]:
                    return False
                else:
                    row[r].append(board[r][c])
                if board[r][c] in col[c]:
                    return False
                else:
                    col[c].append(board[r][c])
                if board[r][c] in quad[(r // 3, c // 3)]:
                    return False
                else:
                    quad[(r // 3, c // 3)].append(board[r][c])
        return True
                
                
                
                
