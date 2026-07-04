# [[1, 5], [2, 4], [3, 8], [6, 7], [10, 11]]
# [[1, 8], [10, 11]]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            prevEnd = res[-1][1]
            if prevEnd >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        
        return res