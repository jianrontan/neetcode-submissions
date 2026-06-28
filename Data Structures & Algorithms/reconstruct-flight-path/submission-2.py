from collections import defaultdict, deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(deque)
        for from_i, to_i in sorted(tickets):
            adj[from_i].append(to_i)
        
        res = []
        def dfs(from_i):
            while adj[from_i]:
                to_i = adj[from_i].popleft()
                dfs(to_i)
            res.append(from_i)
        
        dfs("JFK")
        return res[::-1]