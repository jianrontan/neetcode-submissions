class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        iStart, iEnd = intervals[0]

        res = 0
        for jStart, jEnd in intervals[1:]:
            if iEnd > jStart:
                if iEnd > jEnd:
                    iStart, iEnd = jStart, jEnd
                res += 1
            else:
                iStart, iEnd = jStart, jEnd
        
        return res