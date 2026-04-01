# [3,4,2,1,8,4,2]

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heapq.heappush(heap, -stones[i])
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            newStone = max(stone1 - stone2, stone2 - stone1)
            if newStone > 0:
                heapq.heappush(heap, -newStone)
        if heap:
            return -heap[0]
        else:
            return 0