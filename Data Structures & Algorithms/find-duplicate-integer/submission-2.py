#  0  1  2  3  4
# [1, 3, 4, 2, 2]

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while True:
            if i + 1 == nums[i]:
                i += 1
            else:
                replacement = nums[nums[i] - 1]
                if replacement == nums[i]:
                    return replacement
                nums[nums[i] - 1] = nums[i]
                nums[i] = replacement