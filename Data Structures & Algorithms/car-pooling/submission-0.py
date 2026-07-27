import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        initPassengers, initFrom, initTo = trips[0]
        heap = [(initTo, initPassengers)]
        cur = initPassengers
        
        for numPassengers, curTime, alightTime in trips[1:]:
            while heap and heap[0][0] <= curTime:
                alight = heap[0][-1]
                heapq.heappop(heap)
                cur -= alight
            cur += numPassengers
            if cur > capacity:
                return False
            heapq.heappush(heap, (alightTime, numPassengers))

        return True