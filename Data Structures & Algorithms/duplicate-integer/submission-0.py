class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for i in range(len(nums)):
            if nums[i] in numsSet:
                return True
            else:
                numsSet.add(nums[i])
        return False