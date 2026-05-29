class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        partition = 0
        while left < right:
            mid = (left + right) // 2
            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        partition = right

        if target <= nums[-1]:
            left, right = partition, len(nums) - 1
        else:
            left, right = 0, partition - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        
        if left == right and nums[left] == target:
            return left
        return -1