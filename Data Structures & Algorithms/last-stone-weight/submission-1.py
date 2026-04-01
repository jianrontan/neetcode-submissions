import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            newStone = stone1 - stone2
            if newStone > 0:
                heapq.heappush(heap, -newStone)
        if heap:
            return -heap[0]
        else:
            return 0