import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [[-count, char] for char, count in counts.items()]
        heapq.heapify(heap)

        cooling = deque()
        cycles = 0

        while heap or cooling:
            cycles += 1

            while cooling and cooling[0][2] <= cycles:
                task = cooling.popleft()
                heapq.heappush(heap, [task[0], task[1]])
            
            if heap:
                task = heapq.heappop(heap)
                task[0] += 1
                if task[0] < 0:
                    cooling.append([task[0], task[1], cycles + n + 1])
        
        return cycles