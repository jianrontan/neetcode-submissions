import heapq

class MedianFinder:

    def __init__(self):
        self.sml = []
        self.big = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.sml, -num)
        if len(self.sml) > 0 and len(self.big) > 0 and -self.sml[0] > self.big[0]:
            heapq.heappush(self.big, -heapq.heappop(self.sml))
        if len(self.big) > len(self.sml):
            while len(self.big) > len(self.sml):
                heapq.heappush(self.sml, -heapq.heappop(self.big))
        elif len(self.sml) > len(self.big):
            while len(self.sml) > len(self.big) + 1:
                heapq.heappush(self.big, -heapq.heappop(self.sml))

    def findMedian(self) -> float:
        n = len(self.sml) + len(self.big)
        even = n % 2 == 0
        if even and n > 0:
            return (-self.sml[0] + self.big[0]) / 2
        elif not even and n > 0:
            return -self.sml[0]
        else:
            return 0