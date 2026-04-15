class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def sub(arr: List[int], idx: int) -> None:
            res.append(arr[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                arr.append(nums[i])
                sub(arr[:], i + 1)
                arr.pop()
        
        sub([], 0)
        return res