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
        print("left, right: ", left, ", ", right)
        while left < right:
            mid = (left + right) // 2
            print("mid: ", mid)
            if nums[left] < nums[mid]:
                print("left: ", nums[left], " < ", "mid: ", nums[mid])
                left = mid
            elif nums[left] > nums[mid]:
                print("left: ", nums[left], " > ", "mid: ", nums[mid])
                right = mid
            else:
                print("left: ", nums[left], " = ", "mid: ", nums[mid])
                return nums[right]
        return nums[left]