class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        row, col = len(grid), len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        self.curSize = 0
        def discoverIsland(i, j):
            if not visited[i][j] and grid[i][j] == 1:
                visited[i][j] = True
                self.curSize += 1
                if i - 1 >= 0:
                    discoverIsland(i - 1, j)
                if j - 1 >= 0:
                    discoverIsland(i, j - 1)
                if i + 1 < row:
                    discoverIsland(i + 1, j)
                if j + 1 < col:
                    discoverIsland(i, j + 1)
        for i in range(row):
            for j in range(col):
                self.curSize = 0
                discoverIsland(i, j)
                res = max(self.curSize, res)
        return res