class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        left, right = 2, 3
        for i in range(3, n):
            steps = left + right
            left = right
            right = steps
        return steps