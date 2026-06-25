class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
                rank[rootX] += 1
                return True
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
                rank[rootY] += 1
                return True
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
                return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return False

        return True