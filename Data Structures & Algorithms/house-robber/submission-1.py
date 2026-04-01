# e o    e     o     e
# 4 6    2     3     5      1       1       2       4       5      6
# 4 6  4+2=6 3+6=9 5+6=11 1+9=10 1+11=12 2+11=13 4+12=16 5+13=18 6+16=22
# 6 5    1     4     6 = 22
# 4 2    5     1     4     6 = 22

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        evenNear = nums[0]
        evenFar = 0
        oddNear = nums[1]
        oddFar = 0
        for i in range(2,len(nums)):
            if i % 2 == 0: # even index
                evenFar = evenNear
                if evenNear > oddFar:
                    evenNear = nums[i] + evenNear
                else:
                    evenNear = nums[i] + oddFar
            else:
                oddFar = oddNear
                if oddNear > evenFar:
                    oddNear = nums[i] + oddNear
                else:
                    oddNear = nums[i] + evenFar
        return max(evenNear, oddNear)