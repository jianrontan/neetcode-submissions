class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.cache = [-1 for _ in range(len(cost))]
        return min(self.dfs(0), self.dfs(1))

    def dfs(self, index: int) -> int:
        if index == len(self.cost) - 1 or index == len(self.cost) - 2:
            return self.cost[index]
        if self.cache[index] != -1:
            return self.cache[index]
        cost = self.cost[index] + min(self.dfs(index + 1), self.dfs(index + 2))
        self.cache[index] = cost
        return cost