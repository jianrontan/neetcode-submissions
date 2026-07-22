class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[None for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                up = dp[r-1][c] if r > 0 else float('inf')
                left = dp[r][c-1] if c > 0 else float('inf')
                dp[r][c] = grid[r][c] + min(up, left)
        
        return dp[m - 1][n - 1]