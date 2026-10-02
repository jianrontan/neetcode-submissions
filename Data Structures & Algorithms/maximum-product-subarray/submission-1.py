# 3 4 -5 2 -1 6 -10 4 2 -1 7 - 8 2

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        zero = False

        left = 1
        leftMax = nums[0]
        for num in nums:
            if num != 0:
                left *= num
                leftMax = max(left, leftMax)
            else:
                left = 1
                zero = True
        
        right = 1
        rightMax = nums[-1]
        for num in reversed(nums):
            if num != 0:
                right *= num
                rightMax = max(right, rightMax)
            else:
                right = 1
                zero = True
        
        return max(leftMax, rightMax) if not zero else max(leftMax, rightMax, 0)