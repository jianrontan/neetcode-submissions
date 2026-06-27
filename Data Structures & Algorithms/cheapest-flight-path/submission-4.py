from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        # Create adjacendy list
        for a, b, price in flights:
            adj[a].append((b, price))
        
        # price to get to i from src
        prices = [float('inf')] * n
        prices[src] = 0

        # create the queue
        queue = deque([(src, 0)])
        stops = 0

        # while there are still paths and haven't exhausted number of stops
        while queue and stops <= k:
            size = len(queue)
            # go queue size times to track num of stops
            for _ in range(size):
                a, cost = queue.popleft()
                for b, price in adj[a]:
                    if cost + price < prices[b]:
                        # update shortest path to b
                        prices[b] = cost + price
                        # follow shortest path
                        queue.append((b, cost + price))
            
            # increment num of stops
            stops += 1
        
        return prices[dst] if prices[dst] != float('inf') else -1