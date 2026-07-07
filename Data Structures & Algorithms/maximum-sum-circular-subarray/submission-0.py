class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        cur_max, max_kadane = 0, nums[0]
        cur_min, min_kadane = 0, nums[0]

        for x in nums:
            cur_max = max(x, cur_max + x)
            max_kadane = max(max_kadane, cur_max)
            cur_min = min(x, cur_min + x)
            min_kadane = min(min_kadane, cur_min)
            total += x

        if max_kadane < 0:
            return max_kadane
        return max(max_kadane, total - min_kadane)