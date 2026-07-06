class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]
        cache[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        if cache[0][0] == 0:
            return 0

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    cache[r][c] = 0
                    continue
                if r > 0:
                    cache[r][c] += cache[r - 1][c]
                if c > 0:
                    cache[r][c] += cache[r][c - 1]
        
        return cache[m - 1][n - 1]