class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = [[None for _ in range(n)] for _ in range(m)]

        def dp(r, c):
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            if cache[r][c] is not None:
                return cache[r][c]
            down, right = float('inf'), float('inf')
            if r < m - 1:
                down = dp(r + 1, c)
            if c < n - 1:
                right = dp(r, c + 1)
            cache[r][c] = grid[r][c] + min(down, right)
            return cache[r][c]
        
        return dp(0, 0)