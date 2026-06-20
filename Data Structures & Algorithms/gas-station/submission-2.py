class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        count, cur, i = 0, 0, 0
        while count < len(gas):
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                count = 0
            else:
                count += 1
            i += 1
            if i >= len(gas):
                i = 0
        
        return i