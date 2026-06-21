import math

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        
        matchsticks.sort(reverse=True)
        side = sum(matchsticks) // 4
        sides = [0 for _ in range(4)]

        def backtrack(i):
            if i == len(matchsticks):
                return True
            for s in range(4):
                if s > 0 and sides[s] == sides[s - 1]:
                    continue
                if sides[s] + matchsticks[i] <= side:
                    sides[s] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[s] -= matchsticks[i]
            return False
        
        return backtrack(0)