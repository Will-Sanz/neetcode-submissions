class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row = len(matrix) - 1
        for r in range(len(matrix)):
            if matrix[r][0] == target:
                return True
            if matrix[r][0] > target:
                row = r - 1
                break
        if len(matrix) > 1 and row == -1:
            return False

        if row < 0:
            return False

        arr = matrix[row]
        
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return True
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
            
        