class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = [{} for _ in range(len(nums))]

        def dp(idx, val):
            if val in cache[idx]:
                return cache[idx][val]
            
            if idx == len(nums) - 1:
                if val == target and nums[idx] == 0:
                    return 2
                elif val + nums[idx] == target or val - nums[idx] == target:
                    return 1
                else:
                    return 0
            
            cache[idx][val] = dp(idx + 1, val + nums[idx]) + dp(idx + 1, val - nums[idx])

            return cache[idx][val]
        
        return dp(0, 0)