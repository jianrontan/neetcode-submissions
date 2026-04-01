class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        number = [1, 2, 3]
        for i in range(3, n):
            steps = number[i-2] * 2 + number[i-1] - number[i - 2]
            number.append(steps)
        return number[-1]