import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = [(grid[0][0], 0, 0)]
        res = grid[0][0]
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        visited = set()
        while queue:
            height, r, c = heapq.heappop(queue)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            res = max(res, height)
            if r == n - 1 and c == n - 1:
                return res
            for lr, ud in dirs:
                if 0 <= r + lr < n and 0 <= c + ud < n:
                    heapq.heappush(queue, (grid[r + lr][c + ud], r + lr, c + ud))