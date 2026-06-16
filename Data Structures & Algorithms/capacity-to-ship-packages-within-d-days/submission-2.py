class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minWeight, maxWeight = max(weights), sum(weights)
        res = float('inf')

        while minWeight <= maxWeight:
            mid = (minWeight + maxWeight) // 2

            dayCount = 0
            curWeight = 0
            for weight in weights:
                curWeight += weight
                if curWeight > mid:
                    dayCount += 1
                    curWeight = weight
            dayCount += 1
            
            if dayCount > days:
                minWeight = mid + 1
            elif dayCount <= days:
                maxWeight = mid - 1
                res = min(res, mid) # why need?
        
        return res