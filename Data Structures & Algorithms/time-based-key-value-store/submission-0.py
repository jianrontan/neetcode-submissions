class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timeline = self.timeMap.get(key, [])
        left, right = 0, len(timeline) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            if timeline[mid][0] <= timestamp:
                res = timeline[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return res