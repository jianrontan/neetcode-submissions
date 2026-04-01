class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        maxP = 0
        for price in prices:
            if price < minP:
                minP = price
            curMax = price - minP
            if curMax > maxP:
                maxP = curMax
        return maxP