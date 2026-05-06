import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return math.sqrt(x*x + y*y)
        
        for i in range(len(points)):
            points[i] = (distance(points[i][0], points[i][1]), points[i])
        heapq.heapify(points)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(points)[1])
        
        return res