class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1 for j in range(n + 1)]

        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return True
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
                return False
            elif rank[rootY] > rank[rootX]:
                parent[rootX] = rootY
                return False
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
                return False
        
        for u, v in edges:
            res = union(u, v)
            if res:
                return [u, v]