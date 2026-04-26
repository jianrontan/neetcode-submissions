from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def findLand(i, j, distance):
            if i - 1 >= 0:
                if grid[i-1][j] == 2147483647:
                    grid[i-1][j] = distance
                    queue.append((i-1, j, distance + 1))
            if j - 1 >= 0:
                if grid[i][j-1] == 2147483647:
                    grid[i][j-1] = distance
                    queue.append((i, j-1, distance + 1))
            if i + 1 < len(grid):
                if grid[i+1][j] == 2147483647:
                    grid[i+1][j] = distance
                    queue.append((i+1, j, distance + 1))
            if j + 1 < len(grid[0]):
                if grid[i][j+1] == 2147483647:
                    grid[i][j+1] = distance
                    queue.append((i, j+1, distance + 1))
        
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j, 1))
        
        while len(queue) > 0:
            params = queue.popleft()
            findLand(params[0], params[1], params[2])