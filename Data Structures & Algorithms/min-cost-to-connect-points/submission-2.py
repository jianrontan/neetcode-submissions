import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def distance(p1, p2):
            return abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1])

        visited = set()
        heap = [(0, 0)]
        res = 0

        while heap:
            dist, idx = heapq.heappop(heap)

            if idx in visited:
                continue

            res += dist
            visited.add(idx)

            for i in range(len(points)):
                if i == idx:
                    continue
                if i not in visited:
                    heapq.heappush(heap, (distance(i, idx), i))
        
        return res