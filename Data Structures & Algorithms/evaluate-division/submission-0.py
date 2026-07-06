from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        for i in range(len(equations)):
            u, v = equations[i]
            value = values[i]
            adjList[u].append((value, v))
            adjList[v].append((1 / value, u))
        
        def dfs(c, d, value):
            if c in visited:
                return -1
            visited.add(c)
            if len(adjList[c]) == 0:
                return -1
            for v, adj in adjList[c]:
                if adj == d:
                    return value * v
                ans = dfs(adj, d, value * v)
                if ans != -1:
                    return ans
            return -1
        
        res = []
        for c, d in queries:
            visited = set()
            res.append(dfs(c, d, 1))
        
        return res