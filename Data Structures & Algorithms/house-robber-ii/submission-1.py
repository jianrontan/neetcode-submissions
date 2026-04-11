class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev2, prev1 = 0, 0
        for i in range(len(nums) - 1):
            prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
        prev22, prev11 = 0, 0
        for i in range(1, len(nums)):
            prev22, prev11 = prev11, max(prev11, prev22 + nums[i])
        return max(prev1, prev11)