from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            succ = succProb[i]
            adj[u].append((-succ, v))
            adj[v].append((-succ, u))
        
        visited = set()
        queue = [(-1, start_node)]
        while queue:
            succ, cur = heapq.heappop(queue)
            if cur == end_node:
                return -succ
            if cur in visited:
                continue
            visited.add(cur)

            for vSucc, vCur in adj[cur]:
                heapq.heappush(queue, (-(vSucc * succ), vCur))
        
        return 0