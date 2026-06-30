import heapq

# dijkstra
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = [(grid[0][0], 0, 0)]
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        visited = set()
        while queue:
            height, r, c = heapq.heappop(queue)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == n - 1 and c == n - 1:
                return height
            for lr, ud in dirs:
                nr, nc = r + lr, c + ud
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(queue, (max(height, grid[nr][nc]), nr, nc))