# e o    e     o     e
# 4 6    2     3     5      1       1       2       4       5      6
# 4 6  4+2=6 3+6=9 5+6=11 1+9=10 1+11=12 2+11=13 4+12=16 5+13=18 6+16=22
# 6 5    1     4     6 = 22
# 4 2    5     1     4     6 = 22

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        return prev1