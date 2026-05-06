import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i, (x, y) in enumerate(points):
            dist = x*x + y*y
            heapq.heappush(heap, (-dist, i, x, y))
            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for _, _, x, y in heap]