class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowerRow = 0
        cols, rows = len(matrix[0]), len(matrix)
        upperRow = rows - 1
        while lowerRow <= upperRow:
            iRow = (lowerRow + upperRow) // 2
            if target < matrix[iRow][0]:
                upperRow = iRow - 1
            elif target > matrix[iRow][cols - 1]:
                lowerRow = iRow + 1
            else:
                return self.searchRow(matrix[iRow], target)
        return False

    def searchRow(self, row: List[int], target: int) -> bool:
        left, right = 0, len(row) - 1
        while left <= right:
            i = (left + right) // 2
            if target < row[i]:
                right = i - 1
            elif target > row[i]:
                left = i + 1
            else:
                return True
        return False