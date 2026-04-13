class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 1:
            return []
        self.res = [[]]
        for i in range(len(nums)):
            self.sub([nums[i]], nums[i + 1:])
        return self.res

    def sub(self, subArr: List[int], arr: List[int]) -> None:
        self.res.append(subArr)
        for i in range(len(arr)):
            self.sub(subArr + [arr[i]], arr[i + 1:])