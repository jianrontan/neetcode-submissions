import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        left, right = 1, maxPile
        res = math.inf
        while left <= right:
            pileSize = (right + left) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / pileSize)
            if time <= h:
                if pileSize < res:
                    res = pileSize
                right = pileSize - 1
            else:
                left = pileSize + 1
        return res