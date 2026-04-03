"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# starts      # ends
# 012345678   # 012345678
# 11111       #   11
#  11111      # 11111
#   11        #  11111
#      1111   #      1111

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        lenI = len(intervals)
        start = sorted(intervals, key=lambda x: x.start)
        end = sorted(intervals, key=lambda x: x.end)
        s, e = 0, 0
        res = 0
        count = 0
        for i in range(lenI):
            curS = s
            if start[s].start < end[e].end:
                s += 1
                count += 1
                res = max(count, res)
            else:
                e += 1
                count -= 1
        return res