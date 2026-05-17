class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for num in nums:
            cur += num
            cur = max(0, cur)
            res = max(cur, res)
        
        if res == 0:
            return max(nums)
        
        return res