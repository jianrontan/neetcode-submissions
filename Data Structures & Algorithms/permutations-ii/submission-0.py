class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
            unique = set()
            for i in range(len(nums)):
                if used[i] or nums[i] in unique:
                    continue
                unique.add(nums[i])
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False
        
        backtrack([], used = [False for _ in range(len(nums))])
        
        return res