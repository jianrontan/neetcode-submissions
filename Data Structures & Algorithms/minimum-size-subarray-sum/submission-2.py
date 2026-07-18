class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        count = 0
        res = float('inf')

        while right < len(nums):
            count += nums[right]
            while count >= target:
                res = min(res, (right - left) + 1)
                count -= nums[left]
                left += 1
            right += 1
        
        return 0 if res == float('inf') else res