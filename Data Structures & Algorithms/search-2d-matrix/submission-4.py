class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m - 1
        while l <= r:
            rowMid = l + (r - l) // 2
            if matrix[rowMid][n - 1] == target:
                return True
            elif matrix[rowMid][n - 1] > target:
                r = rowMid - 1
            else:
                l = rowMid + 1
        if l == m:
            return False
        row = l
        l = 0
        r = n - 1
        while l <= r:
            colMid = l + (r - l) // 2
            if matrix[row][colMid] == target:
                return True
            elif matrix[row][colMid] > target:
                r = colMid - 1
            else:
                l = colMid + 1
        return False