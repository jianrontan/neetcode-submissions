from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for from_i, to_i in tickets:
            adj[from_i].append([to_i, False])
        for key, value in adj.items():
            value.sort()
        
        res = []
        def dfs(from_i):
            res.append(from_i)
            if len(res) == len(tickets) + 1:
                return True
            for i in range(len(adj[from_i])):
                to_i, visited = adj[from_i][i]
                if not visited:
                    adj[from_i][i][1] = True
                    if dfs(to_i):
                        return True
                    adj[from_i][i][1] = False
            res.pop()
            return False
        
        dfs("JFK")
        
        return res