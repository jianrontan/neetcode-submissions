class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:

            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                if nums[0] > target and nums[0] <= nums[mid]:
                    left = mid + 1
                elif nums[0] > target and nums[0] > nums[mid]:
                    right = mid
                else:
                    right = mid
            elif nums[mid] < target:
                if nums[-1] < target and nums[-1] >= nums[mid]:
                    right = mid
                elif nums[-1] < target and nums[-1] < nums[mid]:
                    left = mid + 1
                else:
                    left = mid + 1
        
        if left == right and nums[left] == target:
            return left
        return -1