class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        cache = [[None for _ in range(n)] for _ in range(n)]

        def optimal(l, r):
            if r < 0 or l >= n or l > r:
                return float('-inf')
            if cache[l][r] != None:
                return cache[l][r]
            
            if l + 1 == r:
                cache[l][r] = max(piles[l], piles[r])
                return max(piles[l], piles[r])
            elif l + 1 > r:
                return float('-inf')
            else:
                left = piles[l] - optimal(l + 1, r)
                right = piles[r] - optimal(l, r - 1)
                cache[l][r] = max(left, right)
                return max(left, right)
        
        return optimal(0, n - 1) > 0