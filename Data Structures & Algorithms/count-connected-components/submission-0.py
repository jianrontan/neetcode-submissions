class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def findParent(node):
            if parent[node] != node:
                parent[node] = findParent(parent[node])
            return parent[node]
        
        def union(x, y):
            rootX, rootY = findParent(x), findParent(y)
            if rootX == rootY:
                return False
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        
        res = n
        for edge in edges:
            if union(edge[0], edge[1]):
                res -= 1
        
        return res