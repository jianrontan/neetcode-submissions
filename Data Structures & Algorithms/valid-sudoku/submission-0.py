class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        sqrSets = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell != ".":
                    if cell in rowSets[i] or cell in colSets[j] or cell in sqrSets[(i//3)*3+(j//3)]:
                        return False
                    rowSets[i].add(cell)
                    colSets[j].add(cell)
                    sqrSets[(i//3)*3+(j//3)].add(cell)
        return True