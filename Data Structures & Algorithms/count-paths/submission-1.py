class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 1
        self.rows, self.cols = m, n
        self.cache = [[-1 for _ in range(n)] for _ in range(m)]
        return self.paths(0,0)
        
    def paths(self, row: int, col: int) -> int:
        if (row+1 == self.rows-1 and col == self.cols-1) or (row == self.rows-1 and col+1 == self.cols-1):
            return 1
        if self.cache[row][col] != -1:
            return self.cache[row][col]
        paths = 0
        if row < self.rows - 1:
            paths += self.paths(row+1, col)
        if col < self.cols - 1:
            paths += self.paths(row, col+1)
        self.cache[row][col] = paths
        return paths