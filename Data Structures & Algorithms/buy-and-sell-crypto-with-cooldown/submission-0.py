class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cache = [[-1 for _ in range(len(prices))] for _ in range(2)]

        def search(idx, holding):
            if idx >= len(prices):
                return 0
            if holding:
                if cache[0][idx] != -1:
                    return cache[0][idx]
                sell = prices[idx] + search(idx + 2, False)
                hold = search(idx + 1, True)
                curMax = max(sell, hold)
                cache[0][idx] = curMax
                return curMax
            else:
                if cache[1][idx] != -1:
                    return cache[1][idx]
                buy = search(idx + 1, True) - prices[idx]
                nothing = search(idx + 1, False)
                curMax = max(buy, nothing)
                cache[1][idx] = curMax
                return curMax
            
        return search(0, False)