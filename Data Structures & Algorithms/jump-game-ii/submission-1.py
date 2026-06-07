class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        res = 0
        maxRange = 0

        while left < len(nums) and right < len(nums):
            if maxRange == len(nums) - 1:
                return res
            maxRange = 0
            for i in range(left, right + 1):
                maxRange = max(maxRange, i + nums[i])
            left = right + 1
            right = maxRange
            res += 1
        
        return res