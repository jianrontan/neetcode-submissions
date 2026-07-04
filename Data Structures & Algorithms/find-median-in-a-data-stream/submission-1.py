import heapq

class MedianFinder:

    def __init__(self):
        self.sml = []
        self.big = []

    def addNum(self, num: int) -> None:
        print(" ")
        print("addNum:", num)
        heapq.heappush(self.sml, -num)
        if len(self.sml) > 0 and len(self.big) > 0 and -self.sml[0] > self.big[0]:
            heapq.heappush(self.big, -heapq.heappop(self.sml))
        if len(self.big) > len(self.sml):
            while len(self.big) > len(self.sml):
                heapq.heappush(self.sml, -heapq.heappop(self.big))
        elif len(self.sml) > len(self.big):
            while len(self.sml) > len(self.big) + 1:
                heapq.heappush(self.big, -heapq.heappop(self.sml))
        print("sml:", self.sml)
        print("big:", self.big)

    def findMedian(self) -> float:
        print(" ")
        print("findMedian")
        n = len(self.sml) + len(self.big)
        even = n % 2 == 0
        if even and n > 0:
            print((-self.sml[0] + self.big[0]) / 2)
            return (-self.sml[0] + self.big[0]) / 2
        elif not even and n > 0:
            print(-self.sml[0])
            return -self.sml[0]
        else:
            print(0)
            return 0