class Solution:
    def solve(self, board: List[List[str]]) -> None:
        surrounded = [[True for _ in range(len(board[0]))] for _ in range(len(board))]
        def findOs(i, j):
            if surrounded[i][j] and board[i][j] == "O":
                surrounded[i][j] = False
                coordinates = [[i+1,j], [i,j+1], [i-1,j], [i,j-1]]
                for r, c in coordinates:
                    if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
                        findOs(r, c)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                    findOs(i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if surrounded[i][j] and board[i][j] == "O":
                    board[i][j] = "X"