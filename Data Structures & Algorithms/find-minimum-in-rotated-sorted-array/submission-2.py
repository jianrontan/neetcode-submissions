# 7 8 9 10 11 12 13 14 3 4 5 6
# 7 8 9 10 11 [12] 13 14 3 4 5 6
# 13 14 [3] 4 5 6
# 13 [14] 3
# [14] 3

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        lenNums = len(nums)
        left, right = 0, lenNums - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                left = mid
            elif nums[left] > nums[mid]:
                right = mid
            else:
                return nums[right]
        return nums[left]