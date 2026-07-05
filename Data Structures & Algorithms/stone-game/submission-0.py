class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        cache = [[float('-inf') for _ in range(n)] for _ in range(n)]

        def optimal(l, r):
            if 0 > l >= n - 1 or 0 > r >= n - 1:
                return float('-inf')
            if cache[l][r] != float('-inf'):
                return cache[l][r]
            if l + 1 == r:
                cache[l][r] = max(piles[l], piles[r])
                return max(piles[l], piles[r])
            elif l + 1 > r:
                return float('-inf')
            else:
                left = optimal(l + 1, r) + piles[l]
                right = optimal(l, r - 1) + piles[r]
                cache[l][r] = max(left, right)
                return max(left, right)
        
        alice = optimal(0, n - 1)
        bob = max(optimal(1, n - 1), optimal(0, n - 2))

        return alice > bob