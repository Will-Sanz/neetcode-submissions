class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0]) - 1 # column boundaries
        t, b = 0, len(matrix) - 1 # row boundaries

        res = []

        while l <= r and t <= b:
            if t == b:
                for i in range(l, r + 1):
                    res.append(matrix[t][i])
                break
            if r == l:
                for i in range(t, b + 1):
                    res.append(matrix[i][l])
                break
            for i in range(l, r):
                res.append(matrix[t][i])
            for i in range(t, b):
                res.append(matrix[i][r])
            for i in range(r, l, -1):
                res.append(matrix[b][i])
            for i in range(b, t, -1):
                res.append(matrix[i][l])
            l += 1
            r -= 1
            t += 1
            b -= 1
        
        return res
        



