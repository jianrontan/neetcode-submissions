class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []

        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])

        if sum(diff) < 0:
            return -1

        count, cur, i = 0, 0, 0
        while count < len(diff):
            cur += diff[i]
            if cur < 0:
                cur = 0
                count = 0
            else:
                count += 1
            i += 1
            if i >= len(diff):
                i = 0
        
        return i