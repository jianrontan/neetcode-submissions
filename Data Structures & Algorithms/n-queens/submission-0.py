class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        free = [[0 for _ in range(n)] for _ in range(n)]

        def fillUnfill(r, c, val):
            if val == -1:
                free[r][c] = 2

            for i in range(n):
                free[r][i] += val
                free[i][c] += val
            
            if val == 1:
                free[r][c] = "Q"

            dirs = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                while 0 <= nr < n and 0 <= nc < n:
                    free[nr][nc] += val
                    nr, nc = nr + dr, nc + dc

        def addToRes():
            sol = []
            for r in range(n):
                row = ""
                for c in range(n):
                    if free[r][c] == "Q":
                        row += "Q"
                    else:
                        row += "."
                sol.append(row)
            res.append(sol)

        def dp(r):
            for col in range(n):
                if free[r][col] == 0:
                    fillUnfill(r, col, 1)
                    if r == n - 1:
                        addToRes()
                    else:
                        dp(r + 1)
                    fillUnfill(r, col, -1)
        
        dp(0)

        return res