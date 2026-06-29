class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        pos = [0 for _ in range(n * n)]
        for r in range(n):
            for c in range(m):
                pos[grid[r][c]] = (r, c)
        
        parent = [[[r, c] for c in range(m)] for r in range(n)]
        rank = [[1 for _ in range(m)] for _ in range(n)]
        
        def find(r, c):
            if parent[r][c] == [r, c]:
                return [r, c]
            parent[r][c] = find(parent[r][c][0], parent[r][c][1])
            return parent[r][c]
        
        def union(r1, c1, r2, c2):
            pr1, pc1 = find(r1, c1)
            pr2, pc2 = find(r2, c2)
            if pr1 == pr2 and pc1 == pc2:
                return True
            if rank[pr1][pc1] > rank[pr2][pc2]:
                parent[pr2][pc2] = [pr1, pc1]
                return False
            elif rank[pr1][pc1] < rank[pr2][pc2]:
                parent[pr1][pc1] = [pr2, pc2]
                return False
            else:
                parent[pr1][pc1] = [pr2, pc2]
                rank[pr2][pc2] += 1
                return False
        
        for water in range(n * n):
            r, c = pos[water]
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for lr, ud in dirs:
                if 0 <= r + lr < n and 0 <= c + ud < m and grid[r + lr][c + ud] <= water:
                    union(r, c, r + lr, c + ud)
            if find(0, 0) == find(n - 1, m - 1):
                return water