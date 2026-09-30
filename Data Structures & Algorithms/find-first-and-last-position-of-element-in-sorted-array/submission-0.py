# [5,7,7,8,8,10] target 8
# len = 6, mid = 3, right = 3, mid = 1, left = 2, mid = 2, left = 3
# len = 6, mid = 3, left = 3, mid = 4, left = 4, mid = 5, right = 4

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums)
        leftEdge = target - 0.5
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > leftEdge:
                right = mid
            else:
                left = mid + 1
        leftIdx = left
        
        left, right = 0, len(nums)
        rightEdge = target + 0.5
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > rightEdge:
                right = mid
            else:
                left = mid + 1
        rightIdx = left - 1

        if leftIdx >= len(nums) or nums[leftIdx] != target:
            return [-1, -1]
        else:
            return [leftIdx, rightIdx]