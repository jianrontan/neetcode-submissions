class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowerRow = 0
        cols, rows = len(matrix[0]), len(matrix)
        upperRow = rows - 1
        while lowerRow <= upperRow:
            print(" ")
            print("lowerRow: ", matrix[lowerRow], " ", lowerRow, " upperRow: ", matrix[upperRow], " ", upperRow)
            iRow = (lowerRow + upperRow) // 2
            print("iRow: ", matrix[iRow], " ", iRow)
            if target < matrix[iRow][0]:
                print("target < matrix[iRow][cols - 1]")
                upperRow = iRow - 1
            elif target > matrix[iRow][cols - 1]:
                print("target > matrix[iRow][0]")
                lowerRow = iRow + 1
            else:
                return self.searchRow(matrix[iRow], target)
        return False

    def searchRow(self, row: List[int], target: int) -> bool:
        print(" ")
        print("---FOUND THE ROW---")
        print("row: ", row)
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