class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiplier = nums[0]
        output = [1]
        for i in range(1, len(nums)):
            output.append(multiplier)
            multiplier *= nums[i]

        multiplier = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= multiplier
            multiplier *= nums[i]
        
        return output