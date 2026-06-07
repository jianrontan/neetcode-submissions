import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        visited = set()
        heap = [(0, points[0])]
        res = 0

        while heap:
            dist, point = heapq.heappop(heap)

            if tuple(point) in visited:
                continue

            res += dist
            visited.add(tuple(point))

            for other in points:
                if other == point:
                    continue
                if tuple(other) not in visited:
                    heapq.heappush(heap, (distance(other, point), other))
        
        return res