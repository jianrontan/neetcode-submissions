from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for a, b, price in flights:
            adj[a].append((b, price))
        
        prices = [float('inf')] * n
        prices[src] = 0
        queue = deque([(src, 0)])
        stops = 0

        while queue and stops <= k:
            size = len(queue)
            for _ in range(size):
                a, cost = queue.popleft()
                for b, price in adj[a]:
                    if cost + price < prices[b]:
                        prices[b] = cost + price
                        queue.append((b, cost + price))
            stops += 1
        
        return prices[dst] if prices[dst] != float('inf') else -1