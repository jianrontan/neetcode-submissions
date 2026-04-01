class Solution:
    def __init__(self):
        self.visited = []

    def find1s(self, grid: List[List[str]], j: int, i: int):
        lenX = len(grid[0])
        lenY = len(grid)
        if j+1 < lenY:
            if grid[j+1][i] == "1" and self.visited[j+1][i] == False:
                self.visited[j+1][i] = True
                self.find1s(grid, j+1, i)
        if i+1 < lenX:
            if grid[j][i+1] == "1" and self.visited[j][i+1] == False:
                self.visited[j][i+1] = True
                self.find1s(grid, j, i+1)
        if j-1 >= 0:
            if grid[j-1][i] == "1" and self.visited[j-1][i] == False:
                self.visited[j-1][i] = True
                self.find1s(grid, j-1, i)
        if i-1 >= 0:
            if grid[j][i-1] == "1" and self.visited[j][i-1] == False:
                self.visited[j][i-1] = True
                self.find1s(grid, j, i-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        x = len(grid[0])
        y = len(grid)
        for j in range(y):
            visited_row = []
            for i in range(x):
                visited_row.append(False)
            self.visited.append(visited_row)
        
        res = 0
        for j in range(y):
            for i in range(x):
                if grid[j][i] == "1" and self.visited[j][i] == False:
                    self.find1s(grid, j, i)
                    res += 1
        
        return res
