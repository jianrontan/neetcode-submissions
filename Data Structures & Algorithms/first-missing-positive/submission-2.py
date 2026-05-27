class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(-1)
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] < len(nums) and nums[i] != i:
                replaced = nums[nums[i]]
                nums[nums[i]] = nums[i]
                while replaced > 0 and replaced < len(nums) and nums[replaced] != replaced:
                    newReplaced = nums[replaced]
                    nums[replaced] = replaced
                    replaced = newReplaced

        for i in range(1, len(nums)):
            if nums[i] != i:
                return i
        
        return len(nums)