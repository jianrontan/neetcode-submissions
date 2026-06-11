class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def countCoins(amount):
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            minimum = float('inf')
            for coin in coins:
                minimum = min(minimum, countCoins(amount - coin))
            cache[amount] = 1 + minimum
            return 1 + minimum
        
        res = countCoins(amount)
        if res < float('inf'):
            return res
        return -1